import os
import sys
import logging

import pytest

from calculator.src.calculator import Calculator
from calculator.config import config


logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    '[%(asctime)s] ' +
    '[%(filename)s::%(funcName)s:%(lineno)d] ' +
    '[%(levelname)s] %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S')

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


class TestCalculator:

    calc = Calculator()
    x = 6
    y = 2

    def test_add_happy(self):
        expected = 8
        result = self.calc.add(self.x, self.y)
        assert result == expected

    def test_subtract_happy(self):
        expected = 4
        result = self.calc.subtract(self.x, self.y)
        assert result == expected

    def test_multiply_happy(self):
        expected = 12
        result = self.calc.multiply(self.x, self.y)
        assert result == expected

    def test_divide_happy(self):
        expected = 3
        result = self.calc.divide(self.x, self.y)
        assert result == expected
