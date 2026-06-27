import pytest
import requests

from src.streamlit_course.openrouter_client import (
    DEFAULT_MODEL,
    OPENROUTER_CHAT_URL,
    OpenRouterError,
    send_openrouter_message,
)


class FakeResponse:
    def __init__(self, payload, status_code=200):
        self.payload = payload
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError("bad request")

    def json(self):
        return self.payload


def test_send_openrouter_message_posts_chat_completion(monkeypatch):
    calls = []

    def fake_post(url, headers, json, timeout):
        calls.append(
            {
                "url": url,
                "headers": headers,
                "json": json,
                "timeout": timeout,
            }
        )
        return FakeResponse(
            {
                "model": DEFAULT_MODEL,
                "choices": [{"message": {"content": "Hola desde OpenRouter"}}],
                "usage": {"total_tokens": 12},
            }
        )

    monkeypatch.setattr("src.streamlit_course.openrouter_client.requests.post", fake_post)

    reply = send_openrouter_message("Hola", "test-key")

    assert reply.content == "Hola desde OpenRouter"
    assert reply.model == DEFAULT_MODEL
    assert reply.usage == {"total_tokens": 12}
    assert calls[0]["url"] == OPENROUTER_CHAT_URL
    assert calls[0]["headers"]["Authorization"] == "Bearer test-key"
    assert calls[0]["json"]["model"] == DEFAULT_MODEL
    assert calls[0]["json"]["messages"] == [{"role": "user", "content": "Hola"}]


def test_send_openrouter_message_rejects_empty_prompt():
    with pytest.raises(OpenRouterError, match="Escribe una pregunta"):
        send_openrouter_message(" ", "test-key")


def test_send_openrouter_message_rejects_missing_key():
    with pytest.raises(OpenRouterError, match="OPENROUTER_API_KEY"):
        send_openrouter_message("Hola", "")


def test_send_openrouter_message_wraps_http_errors(monkeypatch):
    def fake_post(url, headers, json, timeout):
        return FakeResponse({"error": "bad"}, status_code=401)

    monkeypatch.setattr("src.streamlit_course.openrouter_client.requests.post", fake_post)

    with pytest.raises(OpenRouterError, match="HTTP: 401"):
        send_openrouter_message("Hola", "bad-key")


def test_send_openrouter_message_rejects_malformed_response(monkeypatch):
    def fake_post(url, headers, json, timeout):
        return FakeResponse({"choices": []})

    monkeypatch.setattr("src.streamlit_course.openrouter_client.requests.post", fake_post)

    with pytest.raises(OpenRouterError, match="no devolvió"):
        send_openrouter_message("Hola", "test-key")
