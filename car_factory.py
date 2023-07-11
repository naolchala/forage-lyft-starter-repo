from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CarFactory:
    @staticmethod
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        battery = SpindlerBattery(last_service_date, current_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(engine=engine, battery=battery)

    @staticmethod
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        battery = SpindlerBattery(last_service_date, current_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(engine=engine, battery=battery)

    @staticmethod
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_is_on: bool):
        battery = NubbinBattery(last_service_date, current_date)
        engine = SternmanEngine(warning_light_is_on)
        return Car(engine=engine, battery=battery)

    @staticmethod
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        battery = NubbinBattery(last_service_date, current_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(engine=engine, battery=battery)

    @staticmethod
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        battery = NubbinBattery(last_service_date, current_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(engine=engine, battery=battery)
