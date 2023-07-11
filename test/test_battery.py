import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class TestNubbin(unittest.TestCase):
    def test_battery_needs_service(self):
        today = datetime.today()
        last_serviced = today.replace(year=today.year - 5)
        battery = NubbinBattery(
            current_date=today, last_service_date=last_serviced)
        self.assertTrue(battery.needs_service())

    def test_battery_doesnt_need_service(self):
        today = datetime.today()
        last_serviced = today.replace(year=today.year - 1)
        battery = NubbinBattery(
            current_date=today, last_service_date=last_serviced)
        self.assertFalse(battery.needs_service())


class TestSpindler(unittest.TestCase):
    def test_battery_needs_service(self):
        today = datetime.today()
        last_serviced = today.replace(year=today.year - 4)
        battery = SpindlerBattery(
            current_date=today, last_service_date=last_serviced)
        self.assertTrue(battery.needs_service())

    def test_battery_doesnt_need_service(self):
        today = datetime.today()
        last_serviced = today.replace(year=today.year - 1)
        battery = SpindlerBattery(
            current_date=today, last_service_date=last_serviced)
        self.assertFalse(battery.needs_service())


if __name__ == "__main__":
    unittest.main()
