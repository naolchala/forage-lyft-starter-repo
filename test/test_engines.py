import unittest

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCapulet(unittest.TestCase):
    def test_engine_needs_service(self):
        engine = CapuletEngine(
            last_service_mileage=40000, current_mileage=100000)
        self.assertTrue(engine.needs_service())

    def test_engine_doesnt_need_service(self):
        engine = CapuletEngine(
            last_service_mileage=80000, current_mileage=100000)
        self.assertFalse(engine.needs_service())


class TestSternman(unittest.TestCase):
    def test_engine_needs_service(self):
        engine = SternmanEngine(warning_light_is_on=True)
        self.assertTrue(engine.needs_service())

    def test_engine_doesnt_need_service(self):
        engine = SternmanEngine(warning_light_is_on=False)
        self.assertFalse(engine.needs_service())


class TestWilloughtby(unittest.TestCase):
    def test_engine_needs_service(self):
        engine = WilloughbyEngine(
            last_service_mileage=30000, current_mileage=100000)
        self.assertTrue(engine.needs_service())

    def test_engine_doesnt_need_service(self):
        engine = WilloughbyEngine(
            last_service_mileage=80000, current_mileage=100000)
        self.assertFalse(engine.needs_service())


if __name__ == "__main__":
    unittest.main()
