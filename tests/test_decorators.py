#!/usr/bin/env python3

import unittest
from src.decorators import accepts, encrypt, log, perf
from time import sleep


class TestDecorators(unittest.TestCase):

    def setUp(self):
        pass

    @staticmethod
    @accepts.accepts(str)
    def method_with_str_arg(s):
        return True

    @staticmethod
    @accepts.accepts(str, int)
    def method_with_str_int_args(s, i):
        return True

    def test_accepts_type_error(self):

        with self.assertRaises(TypeError): 
            TestDecorators.method_with_str_arg(4)

    def test_accepts_str(self):

        self.assertTrue(TestDecorators.method_with_str_arg('Spicy Paprika'))

    def test_accepts_str_int(self):

        self.assertTrue(TestDecorators.method_with_str_int_args('Rostislav', 10))

    @staticmethod
    @encrypt.encrypt(2)
    @log.log('log.txt')
    def ceaser_cipher():
        return "Get get get low"

    def test_encrypt(self):
        self.assertEqual(TestDecorators.ceaser_cipher(), "Igv igv igv nqy")


    @staticmethod
    @log.log('log.txt', msg="test data", name="test_log_decorator")
    def log_decorator():
        return True

    def test_log_decorator(self):
        self.assertTrue(TestDecorators.log_decorator())

    @staticmethod
    @perf.performance('performance.log')
    def decorator_performance(s):
        sleep(2)
        return s

    def test_decorator_performance(self):
        self.assertEqual(TestDecorators.decorator_performance('mitko'), 'mitko')


if __name__ == '__main__':
    unittest.main()
