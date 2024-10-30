"""Cuenta Bancaria"""
import inspect

class BankAccount:
    """Clase para la Cuenta Bancaria"""

    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction('Cuenta Creada')

    def _log_transaction(self, message: str):
        """Método para generar logs de nuestro programa

        Args:
            message (str): Mensaje para el log
        """

        caller_method = inspect.currentframe().f_back.f_code.co_name

        if self.log_file:
            with open(self.log_file, 'a', encoding='utf-8') as file:
                file.write(f'{message} - ({caller_method})\n')

    def deposit(self, amount: int):
        """Metodo para realizar depositos en la cuenta

        Args:
            amount (int): Valor a depositar en la cuenta

        Returns:
            int: Valor actualizado del balance
        """
        if amount > 0:
            self.balance += amount
            self._log_transaction(f'- Depositado: {amount}. Balance actual: {self.balance}')

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
                self._log_transaction(f'- Retiro: {amount}. Balance actual: {self.balance}')

            else:
                self._log_transaction('- No hay saldo suficiente en la cuenta.')
                raise ValueError("No hay saldo suficiente en la cuenta.")
        else:
            self._log_transaction('- No hay saldo disponible en la cuenta.')
            raise ValueError("No hay saldo disponible en la cuenta.")

        return self.balance

    def get_balance(self):
        """Método para consultar el saldo de la cuenta

        Returns:
            int: Valor actual del balance
        """
        self._log_transaction(f'- Balance actual: {self.balance}')

        return self.balance

    def transfer(self, target_account: "BankAccount", amount: int):
        """Transferir dinero a otra cuenta

        Args:
            target_account (Objeto BankAcount): Cuenta de Destino
            amount (int): Valor de la transferencia

        Returns:
            int: Valor actual del balance
        """
        if self.balance > 0:
            self.withdraw(amount)
            self._log_transaction(f'- Valor del deposito: {amount}.')

            target_account.deposit(amount)
        else:
            self._log_transaction('- No hay saldo disponible en la cuenta.')
            raise ValueError("No hay saldo disponible en la cuenta.")

        return self.balance
