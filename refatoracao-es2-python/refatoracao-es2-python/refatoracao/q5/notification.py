from abc import ABC, abstractmethod
from datetime import date


class Notification(ABC):

    @abstractmethod
    def subject(self) -> str: ...

    @abstractmethod
    def body(self) -> str: ...

    def render(self) -> str:
        return f"[{date.today()}] {self.subject()}\n{self.body()}"
