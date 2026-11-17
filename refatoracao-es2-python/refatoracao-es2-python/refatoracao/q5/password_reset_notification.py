from refatoracao.q5.notification import Notification


class PasswordResetNotification(Notification):

    def __init__(self, customer_name: str):
        self._customer_name = customer_name

    def subject(self) -> str:
        return "Redefinição de senha"

    def body(self) -> str:
        return f"Olá {self._customer_name}, clique no link para redefinir."
