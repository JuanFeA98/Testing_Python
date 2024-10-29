"""Test para la clase BankAccount"""

import os
import unittest

from src.bank_account import BankAccount


class BankAccountTests(unittest.TestCase):
    """Clase para los tests de BankAccount"""

    def setUp(self) -> None:
        self.account_a = BankAccount(balance=3000, log_file='./Log/transaction_log.txt')
        self.account_b = BankAccount(balance=0)

    def tearDown(self) -> None:
        if os.path.exists(self.account_a.log_file):
            os.remove(self.account_a.log_file)

    def test_deposit(self):
        """Test de deposito en cuenta bancaria"""

        new_balance = self.account_a.deposit(10000)

        assert new_balance == 13000

    def test_withdraw(self):
        """Test de retiro en cuenta bancaria"""
        new_balance = self.account_a.withdraw(2000)

        assert new_balance == 1000

    def test_withdraw_without_sufficient_balance(self):
        """Test de retiro en cuenta bancaria con fondos insuficientes"""
        with self.assertRaises(ValueError) as context:
            self.account_a.withdraw(5000)

        self.assertEqual(
            str(context.exception), "No hay saldo suficiente en la cuenta."
        )

    def test_withdraw_balance_zero(self):
        """Test de retiro en cuenta bancaria sin saldo"""
        with self.assertRaises(ValueError) as context:
            self.account_b.withdraw(4000)

        self.assertEqual(
            str(context.exception), "No hay saldo disponible en la cuenta."
        )

    def test_transfer(self):
        """Test de transferencia a otra cuenta"""
        self.account_a.transfer(self.account_b, 2000)

        assert self.account_a.get_balance() == 1000
        assert self.account_b.get_balance() == 2000

    def test_transfer_without_sufficient_balance(self):
        """Test de transferencia en cuenta bancaria con fondos insuficientes"""
        with self.assertRaises(ValueError) as context:
            self.account_a.transfer(self.account_b, 10000)

        self.assertEqual(
            str(context.exception), "No hay saldo suficiente en la cuenta."
        )

    def test_transfer_balance_zero(self):
        """Test de retiro en cuenta bancaria sin saldo"""
        with self.assertRaises(ValueError) as context:
            self.account_b.transfer(self, 2000)

        self.assertEqual(
            str(context.exception), "No hay saldo disponible en la cuenta."
        )

    def test_transaction_log(self):
        """Test de generación del log"""
        assert os.path.exists(self.account_a.log_file)
