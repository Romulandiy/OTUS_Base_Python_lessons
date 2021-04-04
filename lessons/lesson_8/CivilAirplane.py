from dataclasses import dataclass
from pprint import pprint
from lessons.lesson_8.Airplane import Airplane


@dataclass
class CivilAirplane(Airplane):
    type_of_motor = str  # Тип двигателя
    passenger_capacity = int  # Вместительность пассажиров

    def make_sound(self):
        pprint("Uuuuuu...!")
