from dataclasses import dataclass
from lessons.lesson_8.main_lesson_8 import MeansOfTransport


@dataclass
class Airplane(MeansOfTransport):
    limiting_height: int # Предельная высота

    def make_sound(self):
        pass

    def go(self):
        pass
