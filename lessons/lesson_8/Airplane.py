from dataclasses import dataclass
from lessons.lesson_8.MeansOfTransport import MeansOfTransport


@dataclass
class Airplane(MeansOfTransport):
    limiting_height: int = 0 # Предельная высота

    def make_sound(self):
        pass

    def go(self, instance):
        pass
