from refatoracao.q5.password_reset_notification import PasswordResetNotification


# Classe redundante: não adiciona comportamento
class VIPPasswordResetNotification(PasswordResetNotification):

    def __init__(self, customer_name: str):
        super().__init__(customer_name)
