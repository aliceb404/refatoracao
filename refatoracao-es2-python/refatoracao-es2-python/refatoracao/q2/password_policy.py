from __future__ import annotations


class PasswordPolicy:

    def is_valid(self, password: str | None) -> bool:
        return (
            self._has_min_length(password)
            and self._has_upper(password)
            and self._has_digit(password)
            and self._has_no_spaces(password)
        )

    def _has_min_length(self, p: str | None) -> bool:
        return p is not None and len(p) >= 10

    def _has_upper(self, p: str) -> bool:
        return any(c.isupper() for c in p)

    def _has_digit(self, p: str) -> bool:
        return any(c.isdigit() for c in p)

    def _has_no_spaces(self, p: str) -> bool:
        return " " not in p
