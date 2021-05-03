from dataclasses import dataclass
from pprint import pprint
from lessons.lesson_8.MyException import MyException
from lessons.lesson_8.Ship import Ship


@dataclass
class Motorboat(Ship):
    mast_height: int = 0  # Высота мачты
    sail_area: int = 0  # Площадь полотна паруса

    def make_sound(self):
        pprint("BUIL'K")

    def go(self, instance):
        instance.power_engine()

    def count_of_passengers(self):
        try:
            if not (self.mast_height >= 5 and self.sail_area >= 450 and self.displacement >= 17500):
                raise Exception(MyException.max_passengers())
        except Exception:
            print("Raised an exception", "\n")
        else:
            print("You can take on board more than 4 passengers")
