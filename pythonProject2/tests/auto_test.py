import pytest
from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_succes(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_subtraction_succes(self):
        assert self.calc.subtraction(self, 2, 1) == 1

    def test_division_succes(self):
        assert self.calc.division(self, 2, 2) == 1

    def test_multiply_succes(self):
        assert self.calc.multiply(self, 2, 2) == 4

