from refatoracao.q1.purchase_email_service import (
    Address,
    Purchase,
    PurchaseEmailService,
    PurchaseItem,
)


def test_build_email_should_keep_same_output_after_refactor():
    # TODO: complete asserts para garantir que o texto final não muda após refatorar
    svc = PurchaseEmailService()

    purchase = Purchase(
        "123",
        "Victor",
        [
            PurchaseItem("Caderno", 2, 15.0),
            PurchaseItem("Caneta", 3, 3.5),
        ],
        False,
        "VIP-20",
        Address("Rua A", "10", "Belém", "66000-000"),
    )

    email = svc.build_email(purchase)

    assert "Olá, Victor" in email
    assert "Seu pedido #123" in email
    assert "Caderno" in email
    assert "Endereço de entrega" in email
