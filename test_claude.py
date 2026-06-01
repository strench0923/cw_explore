import os
from pathlib import Path

from anthropic import Anthropic


def load_env_file(path=".env"):
    env_path = Path(path)
    if not env_path.exists():
        return

    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env_file()

api_key = os.environ.get("ANTHROPIC_API_KEY")
if not api_key or api_key == "your_api_key_here":
    raise RuntimeError("Set ANTHROPIC_API_KEY in .env before running this script.")

client = Anthropic(api_key=api_key)

message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude!"}
    ]
)

print(message.content[0].text)
