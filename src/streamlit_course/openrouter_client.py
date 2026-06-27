from dataclasses import dataclass
from typing import Any

import requests


OPENROUTER_CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "openrouter/free"


class OpenRouterError(RuntimeError):
    pass


@dataclass(frozen=True)
class OpenRouterReply:
    content: str
    model: str
    usage: dict[str, Any] | None


def send_openrouter_message(
    prompt: str,
    api_key: str,
    model: str = DEFAULT_MODEL,
    timeout: int = 30,
) -> OpenRouterReply:
    if not prompt.strip():
        raise OpenRouterError("Escribe una pregunta antes de enviar.")
    if not api_key.strip():
        raise OpenRouterError("Configura OPENROUTER_API_KEY o pega una llave temporal.")

    response = requests.post(
        OPENROUTER_CHAT_URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=timeout,
    )

    try:
        response.raise_for_status()
    except requests.HTTPError as error:
        raise OpenRouterError(f"OpenRouter respondió con error HTTP: {response.status_code}") from error

    payload = response.json()
    choices = payload.get("choices", [])
    if not choices:
        raise OpenRouterError("OpenRouter no devolvió una respuesta usable.")

    message = choices[0].get("message", {})
    content = message.get("content", "").strip()
    if not content:
        raise OpenRouterError("OpenRouter devolvió una respuesta vacía.")

    return OpenRouterReply(
        content=content,
        model=payload.get("model", model),
        usage=payload.get("usage"),
    )
