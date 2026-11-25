import tiktoken


def encode_text(text: str) -> list[int]:
    """Encode text with the configured Tiktoken encoding."""
    encoding = tiktoken.get_encoding("o200k_base")
    return encoding.encode(text)


if __name__ == "__main__":
    print(encode_text("I love AI"))