from refatoracao.q2.password_policy import PasswordPolicy


def test_valid_password_examples():
    policy = PasswordPolicy()
    assert policy.is_valid("SenhaForte1")


def test_invalid_password_examples():
    policy = PasswordPolicy()
    assert not policy.is_valid("curta1A")       # < 10
    assert not policy.is_valid("senhaforte1")   # sem maiúscula
    assert not policy.is_valid("SenhaForteX")   # sem dígito
    assert not policy.is_valid("Senha Forte1")  # espaço


def test_refactor_goal_inline_some_helpers():
    # TODO: após refatorar, alguns helpers devem sumir (inline)
    # Este teste não verifica estrutura, só comportamento.
    pass
