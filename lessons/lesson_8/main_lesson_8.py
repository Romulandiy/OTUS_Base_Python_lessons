from pprint import pprint
from typing import Optional

from abc import ABC, abstractmethod
from dataclasses import dataclass

from lessons.lesson_8.PassengerCar import PassengerCar


@dataclass
class MeansOfTransport(ABC):
    weight: int # Вес
    carrying_capacity: int # Грузоподъемность

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def go(self):
        pass


if __name__ == '__main__':
    exm1 = PassengerCar(weight=1370, carrying_capacity=530, number_of_wheels=4)
    print(exm1)
