import pytest

from refatoracao.q10.room_booking import RoomBooking


def test_quote_examples():
    rb = RoomBooking()

    assert rb.quote("B", 1, "101", 8, 10, False, False, 10) == pytest.approx(100.0, abs=0.001)
    assert rb.quote("A", 3, "101", 8, 10, True, True, 50) == pytest.approx(
        (2 * 50.0 + 30 + 20) * 1.15 + 10, abs=0.01
    )
    assert rb.quote("B", 1, "LAB", 8, 10, False, False, 10) == pytest.approx(
        (2 * 50.0) + 40, abs=0.01
    )


def test_refactor_goal_introduce_parameter_object():
    # TODO: introduzir BookingRequest/Room/Schedule e reduzir parâmetros primitivos.
    # Ajuste as chamadas acima se necessário, mantendo os valores esperados.
    pass
