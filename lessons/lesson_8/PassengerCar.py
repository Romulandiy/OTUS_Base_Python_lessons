from dataclasses import dataclass
from pprint import pprint

from lessons.lesson_8.Car import Car
from lessons.lesson_8.MyException import MyException
from attr import attrs, attrib, attr

validator_status_motor = attr.validators.in_(["running", "stop"])


@attrs
# @dataclass
class PassengerCar(Car):
    color = str # Цвет автомобиля
    body_type = str # Тип кузова
    fuel_tank_volume = int # Объем топливного бака
    fuel_remaining_in_tank = int # Количество оставшегося топлива в баке
    status_motor = attrib(default=None, validator=attr.validators(validator_status_motor))

    def make_sound(self):
        pprint("Biiiipppp...!")

    def go(self):
        pass

    def start_motor(self, fuel_tank, remaining_fuel_in_tank):
        if remaining_fuel_in_tank / fuel_tank <= 0.04:
            raise MyException("Not enough fuel in tank")
        else:
            return self.status_motor[0]
