from dataclasses import dataclass
from lessons.lesson_8.Ship import Ship


@dataclass
class Sailboat(Ship):
    mast_height = int  # Высота мачты
    sail_area = int  # Площадь полотна паруса

    def make_sound(self):
        pprint("BUIL'K")