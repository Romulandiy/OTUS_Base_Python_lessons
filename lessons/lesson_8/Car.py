from dataclasses import dataclass
from lessons.lesson_8.main_lesson_8 import MeansOfTransport


@dataclass
class Car(MeansOfTransport):
    number_of_wheels: int # Количество колес

    def make_sound(self):
        pass

    def go(self):
        pass
