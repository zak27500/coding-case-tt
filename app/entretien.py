from app.domain import Entretien


def get_entretien_by_id(id: str, entretiens: list[Entretien]) -> Entretien | None:
    if not entretiens:
        return None
    for entretien in entretiens:
        if entretien.id == id:
            return entretien
    return None
