import json
from pathlib import Path

import pytest

from app.domain import Entretien


@pytest.fixture
def entretien_path() -> Path:
    return Path("E01.json")


@pytest.fixture
def entretien(entretien_path: Path) -> Entretien:
    with open(entretien_path, encoding="utf-8") as f:
        data = json.load(f)
    return Entretien.model_validate(data)


@pytest.fixture
def entretiens(entretien: Entretien) -> list[Entretien]:
    return [entretien]
