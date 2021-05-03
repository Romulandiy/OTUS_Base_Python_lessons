from dataclasses import dataclass
from pprint import pprint
from lessons.lesson_8.Airplane import Airplane


@dataclass
class CivilAirplane(Airplane):
    passenger_capacity: int = 0  # Вместительность пассажиров

    def make_sound(self):
        pprint("Uuuuuu...uuu...!")

    def go(self, instance):
        instance.power_engine_airplane(self.passenger_capacity)
