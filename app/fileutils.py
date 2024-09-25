import json
from pathlib import Path


def json_content(path: str) -> dict:
    filepath = Path(path)

    if not filepath.exists():
        return {}

    with filepath.open() as fp:
        return json.load(fp)
