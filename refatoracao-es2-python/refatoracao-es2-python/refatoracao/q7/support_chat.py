from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    name: str | None
    banned: bool

    def is_banned(self) -> bool:
        return self.banned


class SupportChat:

    def greeting(self, user: User | None) -> str:
        if user is None:
            return "Olá! Quer continuar como visitante?"
        if user.is_banned():
            return "Conta bloqueada. Contate o suporte."
        if user.name is None or user.name.strip() == "":
            return "Olá! Como posso ajudar?"
        return f"Olá, {user.name}! Como posso ajudar?"
