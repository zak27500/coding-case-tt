from app.domain import Entretien
from app.entretien import get_entretien_by_id


def test_get_entretien_by_id(entretiens) -> None:
    expected = "E01"
    result = get_entretien_by_id(expected, entretiens)
    assert isinstance(result, Entretien)
