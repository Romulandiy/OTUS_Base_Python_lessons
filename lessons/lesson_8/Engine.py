from dataclasses import dataclass


@dataclass
class Engine:
    liter: float = 0  # Литраж двигателя
    number_of_pistons: int = 0  # Количество поршней
    maximum_engine_speed: int = 0  # Максимальное количество оборотов двигателя

    def power_engine(self):
        if self.liter >= 2 and self.number_of_pistons >= 6 and self.maximum_engine_speed >= 5000:
            print("Your machine is very, very fast. Congratulations!", "\n")
        else:
            print("Your machine is like a turtle :(", "\n")
