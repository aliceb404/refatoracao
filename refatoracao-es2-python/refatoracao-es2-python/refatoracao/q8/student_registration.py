from __future__ import annotations

import re


class StudentRegistration:

    def __init__(self, name: str | None, email: str | None, phone: str | None,
                 city: str | None, zip_code: str | None):
        self._name = name
        self._email = email
        self._phone = phone
        self._city = city
        self._zip_code = zip_code

    def is_valid(self) -> bool:
        if self._name is None or self._name.strip() == "":
            return False
        if self._email is None or "@" not in self._email:
            return False
        if self._phone is None or len(self._phone) < 10:
            return False
        if self._zip_code is None or not re.fullmatch(r"\d{5}-\d{3}", self._zip_code):
            return False
        return True

    def formatted_contact(self) -> str:
        return f"{self._name} | {self._email} | {self._phone} | {self._city} - {self._zip_code}"
