from dataclasses import dataclass
from lessons.lesson_8.MeansOfTransport import MeansOfTransport


@dataclass
class Car(MeansOfTransport):
    number_of_wheels: int # Количество колес

    def make_sound(self):
        pass

    def go(self, instance):
        pass
