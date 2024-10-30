"""Suites de nuestro programa"""
import unittest
import sys

from test_bank_account import BankAccountTests

sys.path.append('./')
sys.path.append('../')


def bank_account_suite():
    """Suite para la clase de cuenta bancaria"""
    suite = unittest.TestSuite()

    suite.addTest(BankAccountTests('test_deposit'))
    suite.addTest(BankAccountTests('test_withdraw'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())
