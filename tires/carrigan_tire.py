from tires import Tire


class CarriganTire(Tire):
    def __init__(self, worn_range_list: list):
        self.worn_range_list = worn_range_list

    def needs_service(self) -> bool:
        needs_repair = False
        for tire in self.worn_range_list:
            if tire >= 0.9:
                needs_repair = True

        return needs_repair
