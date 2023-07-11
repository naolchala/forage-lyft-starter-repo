from tires import Tire


class OctoprimeTire(Tire):
    def __init__(self, worn_range_list: list):
        self.worn_range_list = worn_range_list

    def needs_service(self) -> bool:
        return sum(self.worn_range_list) >= 3
