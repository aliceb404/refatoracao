import pytest

from refatoracao.q9.order import Customer, Order


def test_final_total_examples():
    vip = Customer(True, 6)
    o1 = Order(vip, 200.0, 0.10)
    assert o1.final_total() == pytest.approx(140.0, abs=0.001)

    regular = Customer(False, 1)
    o2 = Order(regular, 200.0, 0.10)
    assert o2.final_total() == pytest.approx(180.0, abs=0.001)


def test_refactor_goal_move_discount_logic_to_customer_or_policy():
    # TODO: mover lógica de desconto para Customer ou um DiscountPolicy e fazer Order delegar.
    pass
