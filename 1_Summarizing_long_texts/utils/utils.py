import tiktoken


def get_tokens(text: str) -> int:
    """Get the number of tokens in a text by running a tiktoken encoder on it."""
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    tokens = encoding.encode(text)
    return len(tokens)
