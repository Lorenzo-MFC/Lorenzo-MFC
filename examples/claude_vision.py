"""Ask Claude to describe an image, sending it two ways: base64 and URL.

Run:
    pip install -r examples/requirements.txt
    export ANTHROPIC_API_KEY=...   # or sign in once with `ant auth login`
    python examples/claude_vision.py
"""

import base64

import anthropic
import httpx2  # the HTTP library the anthropic SDK 1.x is built on

MODEL = "claude-opus-5-5"
IMAGE_URL = "https://platform.claude.com/docs/images/vision-example.jpg"
IMAGE_MEDIA_TYPE = "image/jpeg"
PROMPT = "What is in the above image?"

# max_tokens is a ceiling, not a charge: you pay only for tokens actually
# produced. Too low a ceiling cuts the answer off (stop_reason "max_tokens").
MAX_TOKENS = 16000


def print_usage(message) -> None:
    """Print token counts for each attempt the API made for this reply.

    When a fallback runs, top-level usage covers only the final attempt;
    usage.iterations lists every attempt (each one billed at its own model's
    rates), so read the cost from there.
    """
    attempts = message.usage.iterations or []
    if not attempts:
        usage = message.usage
        print(f"  tokens: input={usage.input_tokens} output={usage.output_tokens}")
        return
    for attempt in attempts:
        # Compaction entries carry no model name.
        model = getattr(attempt, "model", "-")
        print(
            f"  {attempt.type} on {model}: "
            f"input={attempt.input_tokens} output={attempt.output_tokens}"
        )
    if message.stop_reason != "refusal" and any(
        attempt.type == "fallback_message" for attempt in attempts
    ):
        print(f"  note: {MODEL} declined, so the fallback model {message.model} answered")


def describe(client: anthropic.Anthropic, image_source: dict) -> str:
    """Send one image plus the prompt and return Claude's text answer."""
    message = client.beta.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        # If a safety classifier declines the request, the API re-runs it on
        # Anthropic's recommended fallback model inside the same call.
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "image", "source": image_source},
                    {"type": "text", "text": PROMPT},
                ],
            }
        ],
    )

    print(f"[answered by {message.model}, stop_reason={message.stop_reason}]")
    print_usage(message)

    # The reply can hold other block types (e.g. thinking), so keep only text.
    text = "".join(block.text for block in message.content if block.type == "text")

    # stop_reason says why Claude stopped; always check it before trusting text.
    # (tool_use and pause_turn can't happen here: this script defines no tools.)
    match message.stop_reason:
        case "refusal":
            # Still a refusal with fallbacks="default": the fallback declined too, the
            # category has no recommended fallback, or the fallback was too busy to try.
            # category and explanation can be null; show explanation, never parse it.
            details = message.stop_details
            reason = (details.explanation or details.category) if details else None
            answer = f"(Claude declined this request: {reason or 'no reason given'})"
            if details and details.recommended_model:
                answer += f"\n(you can retry this request on {details.recommended_model})"
            return answer
        case "max_tokens":
            return f"{text}\n\n[Response truncated due to max_tokens limit ({MAX_TOKENS})]"
        case "model_context_window_exceeded":
            return f"{text}\n\n[Response truncated due to context window limit]"
        case _:  # end_turn: a complete answer
            return text or "(Claude returned an empty response)"


def main() -> None:
    client = anthropic.Anthropic()

    # A stop_reason comes with a successful reply; a failed request raises an
    # error instead (the SDK already retries 429 and 5xx errors twice).
    try:
        # Option 1: download the image and send it as base64.
        response = httpx2.get(IMAGE_URL, follow_redirects=True)
        response.raise_for_status()
        image_data = base64.standard_b64encode(response.content).decode("utf-8")
        print("--- Option 1: base64 ---")
        print(
            describe(
                client,
                {"type": "base64", "media_type": IMAGE_MEDIA_TYPE, "data": image_data},
            )
        )

        # Option 2: let the API fetch the image from its URL.
        print("\n--- Option 2: URL ---")
        print(describe(client, {"type": "url", "url": IMAGE_URL}))
    except anthropic.RateLimitError:
        print("Rate limit reached: wait a minute and run the script again.")
    except anthropic.APIStatusError as error:
        print(f"API request failed: {error.message}")
    except anthropic.APIConnectionError:
        print("Could not reach the Claude API: check your network connection.")
    except httpx2.HTTPError as error:
        print(f"Could not download the image: {error}")


if __name__ == "__main__":
    main()
