import pytest

import ai


def test_encode_text_returns_list_of_integers():
    token_ids = ai.encode_text("I love AI")

    assert isinstance(token_ids, list)
    assert token_ids
    assert all(isinstance(token_id, int) for token_id in token_ids)


def test_encode_empty_text_returns_empty_list():
    assert ai.encode_text("") == []


def test_encode_text_is_deterministic():
    text = "Generative AI"

    assert ai.encode_text(text) == ai.encode_text(text)
