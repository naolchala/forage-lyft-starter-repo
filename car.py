from abc import ABC, abstractmethod
from battery import Battery

from engine import Engine
from tires import Tire


class Car(ABC):
    def __init__(self, engine: Engine, battery: Battery, tires: Tire):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()
