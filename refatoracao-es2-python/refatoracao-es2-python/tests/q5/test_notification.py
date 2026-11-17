from refatoracao.q5.vip_password_reset_notification import VIPPasswordResetNotification


def test_render_should_contain_subject_and_body():
    n = VIPPasswordResetNotification("Joelma")
    r = n.render()

    assert "Redefinição de senha" in r
    assert "Olá Joelma" in r


def test_refactor_goal_collapse_hierarchy_remove_redundant_subclass():
    # TODO: após refatorar, VIPPasswordResetNotification deve deixar de existir (ou ganhar comportamento real).
    # O comportamento de renderização deve permanecer.
    pass
