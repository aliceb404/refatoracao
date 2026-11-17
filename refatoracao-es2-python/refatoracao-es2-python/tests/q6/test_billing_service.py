import pytest

from refatoracao.q6.billing_service import BillingService, Plan


def test_price_table_examples():
    svc = BillingService()

    assert svc.monthly_price(Plan.FREE, 10, False) == pytest.approx(0.0, abs=0.001)
    assert svc.monthly_price(Plan.STUDENT, 10, False) == pytest.approx(19.90, abs=0.001)

    assert svc.monthly_price(Plan.PRO, 10, False) == pytest.approx(49.90 + 10 * 1.25, abs=0.01)
    assert svc.monthly_price(Plan.PRO, 250, False) == pytest.approx(
        (49.90 + 250 * 1.25) * 0.95, abs=0.01
    )

    assert svc.monthly_price(Plan.ENTERPRISE, 10, True) == pytest.approx(
        199.90 + 10 * 0.90 + 59.90, abs=0.01
    )


def test_refactor_goal_replace_conditional_with_polymorphism():
    # TODO: após refatorar, o if/elif deve desaparecer (cada plano com sua política).
    # Testes acima devem continuar passando.
    pass
