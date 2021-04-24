from dataclasses import dataclass
from pprint import pprint
from lessons.lesson_8.Car import Car
from lessons.lesson_8.MyException import MyException


@dataclass
class PassengerCar(Car):
    fuel_tank_volume: int = 0  # Объем топливного бака
    fuel_remaining_in_tank: int = 0  # Количество оставшегося топлива в баке
    color: str = ""  # Цвет автомобиля
    body_type: str = ""  # Тип кузова

    def make_sound(self):
        print("Biiiipppp...!", "\n")

    def go(self, instance):
        instance.power_engine()

    @staticmethod
    def start_motor(fuel_tank, remaining_fuel_in_tank):
        try:
            if remaining_fuel_in_tank / fuel_tank <= 0.04:
                raise Exception(MyException.output(fuel_tank, remaining_fuel_in_tank))
        except Exception:
            print("Raised an exception", "\n")
        else:
            pprint(f"remaining_fuel_in_tank / fuel_tank = {remaining_fuel_in_tank}/{fuel_tank} ="
                   f" {remaining_fuel_in_tank / fuel_tank}")
            print("motor is RUNNING", "\n")
