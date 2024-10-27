"""Cuenta Bancaria"""


class BankAccount:
    """Clase para la Cuenta Bancaria"""

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount: int):
        """Metodo para realizar depositos en la cuenta

        Args:
            amount (int): Valor a depositar en la cuenta

        Returns:
            int: Valor actualizado del balance
        """
        if amount > 0:
            self.balance += amount

        return self.balance

    def withdraw(self, amount: int):
        """Método para realizar retiros en la cuenta

        Args:
            amount (int): Valor a retirar

        Returns:
            int: Valor actualizado del balance
        """

        if self.balance > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                raise ValueError("No hay saldo suficiente en la cuenta.")
        else:
            raise ValueError("No hay saldo disponible en la cuenta.")

        return self.balance

    def get_balance(self):
        """Método para consultar el saldo de la cuenta

        Returns:
            int: Valor actual del balance
        """
        return self.balance

    def transfer(self, target_account: "BankAccount", amount: int):
        """Transferir dinero a otra cuenta

        Args:
            target_account (Objeto BankAcount): Cuenta de Destino
            amount (_type_): _description_

        Returns:
            int: Valor actual del balance
        """
        if self.balance > 0:
            self.withdraw(amount)

            target_account.deposit(amount)
        else:
            raise ValueError("No hay saldo disponible en la cuenta.")

        return self.balance
