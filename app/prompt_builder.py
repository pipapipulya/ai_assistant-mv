from app.prompts import get_system_prompt


def build_prompt(role: str, user_message: str, history: list[str] | None = None) -> str:
    system_prompt = get_system_prompt(role)

    history_text = ""
    if history:
        history_text = "\n\nИстория диалога:\n" + "\n".join(history)

    return (
        f"{system_prompt}"
        f"{history_text}\n\n"
        f"Текущее сообщение пользователя: {user_message}\n\n"
        f"Ответь согласно инструкциям выше."
    )