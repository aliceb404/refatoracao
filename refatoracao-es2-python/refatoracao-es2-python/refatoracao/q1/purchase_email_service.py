from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class PurchaseItem:
    name: str
    quantity: int
    unit_price: float


@dataclass(frozen=True)
class Address:
    street: str
    number: str
    city: str
    zip_code: str


@dataclass(frozen=True)
class Purchase:
    id: str
    customer_name: str
    items: list[PurchaseItem]
    is_express: bool
    coupon: str | None
    address: Address


class PurchaseEmailService:

    def build_email(self, purchase: Purchase) -> str:
        parts = []

        parts.append(f"Olá, {purchase.customer_name}!\n\n")
        parts.append(f"Seu pedido #{purchase.id} foi confirmado em {date.today()}.\n\n")

        parts.append("Itens:\n")
        subtotal = 0.0
        for it in purchase.items:
            line = it.unit_price * it.quantity
            subtotal += line
            parts.append(f"- {it.name} ({it.quantity}x) : R$ {line:.2f}\n")

        shipping = 29.90 if purchase.is_express else 14.90
        discount = 0.0
        if subtotal >= 300.0:
            discount = subtotal * 0.10
        if purchase.coupon is not None and purchase.coupon.startswith("VIP"):
            discount += 20.0

        total = subtotal + shipping - discount

        parts.append(f"\nSubtotal: R$ {subtotal:.2f}\n")
        parts.append(f"Frete: R$ {shipping:.2f}\n")
        parts.append(f"Descontos: R$ {discount:.2f}\n")
        parts.append(f"TOTAL: R$ {total:.2f}\n\n")

        parts.append("Endereço de entrega:\n")
        parts.append(f"{purchase.address.street}, {purchase.address.number}\n")
        parts.append(f"{purchase.address.city} - {purchase.address.zip_code}\n\n")

        parts.append("Obrigado por comprar com a gente!\n")
        return "".join(parts)
