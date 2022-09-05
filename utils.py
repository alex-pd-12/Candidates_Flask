import json

def load_json() -> list[dict]:
    """Загружает json кандидатов"""
    with open("candidates.json", "r", encoding="UTF-8") as file:
        candidates = json.load(file)
        return candidates


def format_candidates(candidates: list[dict]) -> str:
    """Форматирование списка кандидатов"""
    result = "<pre>"

    for candidate in candidates:
        result += f"""
            {candidate["name"]}\n
            {candidate["position"]}\n
            {candidate["skills"]}\n
        """
    result += "</pre>"
    return result


def get_all_candidates() -> list[dict]:
    """Возвращает список все кандидатов"""
    return load_json()


def get_candidate_by_id(uid: int) -> dict | None:
    """Возвращает список по id"""
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate["id"] == uid:
            return candidate
    return None


def get_candidate_by_skill(skill: str) -> list[dict]:
    """Возвращает список по skills"""
    candidates = get_all_candidates()
    result = []
    for candidate in candidates:
        if skill in candidate["skills"].lower().split(", "):
            result.append(candidate)
    return result
