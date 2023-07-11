import unittest

from tires.carrigan_tire import CarriganTire
from tires.octoprime_tire import OctoprimeTire


class TestCarrigan(unittest.TestCase):
    def test_tire_needs_service(self):
        tire = CarriganTire([0.81, 0.84, 0.95, 0.76])
        self.assertTrue(tire.needs_service())

    def test_tire_doesnt_needs_service(self):
        tire = CarriganTire([0.81, 0.84, 0.85, 0.76])
        self.assertFalse(tire.needs_service())


class TestOctoprime(unittest.TestCase):
    def test_tire_needs_service(self):
        tire = OctoprimeTire([0.91, 0.94, 0.95, 0.96])
        self.assertTrue(tire.needs_service())

    def test_tire_doesnt_needs_service(self):
        tire = OctoprimeTire([0.50, 0.34, 0.33, 0.46])
        self.assertFalse(tire.needs_service())
