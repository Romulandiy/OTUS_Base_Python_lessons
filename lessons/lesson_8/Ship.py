from dataclasses import dataclass
from lessons.lesson_8.MeansOfTransport import MeansOfTransport


@dataclass
class Ship(MeansOfTransport):
    displacement: int = 0 # Водоизмещение

    def make_sound(self):
        pass

    def go(self):
        pass
