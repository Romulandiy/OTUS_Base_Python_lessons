from abc import ABC, abstractmethod
from dataclasses import dataclass


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
