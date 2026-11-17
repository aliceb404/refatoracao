from refatoracao.q7.support_chat import SupportChat, User


def test_greeting_examples():
    chat = SupportChat()

    assert chat.greeting(None) == "Olá! Quer continuar como visitante?"
    assert chat.greeting(User("Ana", True)) == "Conta bloqueada. Contate o suporte."
    assert chat.greeting(User("  ", False)) == "Olá! Como posso ajudar?"
    assert chat.greeting(User("Victor", False)) == "Olá, Victor! Como posso ajudar?"


def test_refactor_goal_introduce_null_object_remove_null_check():
    # TODO: eliminar if user is None via Null Object / GuestUser mantendo comportamento.
    pass
