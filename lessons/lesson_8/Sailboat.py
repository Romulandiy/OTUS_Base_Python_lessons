from dataclasses import dataclass
from pprint import pprint

from lessons.lesson_8.Ship import Ship


@dataclass
class Sailboat(Ship):
    mast_height: int = 0  # Высота мачты
    sail_area: int = 0  # Площадь полотна паруса

    def make_sound(self):
        pprint("BUIL'K")