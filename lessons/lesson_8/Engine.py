from dataclasses import dataclass, field
from lessons.lesson_8.MyException import MyException


@dataclass
class Engine:
    liter: float = 0  # Литраж двигателя
    number_of_pistons: int = 0  # Количество поршней
    maximum_engine_speed: int = 0  # Максимальное количество оборотов двигателя
    type_motor: str = 'turbojet engine' # Турбореактивный двигатель
    count_turbojet_engine: int = 0 # Количество турбореактивных двигателей
    engine_thrust: list = field(default_factory=list) # Тяга двигателя

    def power_engine(self):
        if self.liter >= 2 and self.number_of_pistons >= 6 and self.maximum_engine_speed >= 5000:
            print("Your machine is very, very fast. Congratulations!", "\n")
        else:
            print("Your machine is like a turtle :(", "\n")

    def power_engine_airplane(self, passenger_capacity):
        self.engine_thrust = [28710, 31780]
        try:
            if self.type_motor == 'turbojet engine' and self.count_turbojet_engine == 4 and passenger_capacity == 660:
                print(f"Your airplane is Boeing 747-400 and engine_thrust = {self.engine_thrust[0]}", "\n")
            elif self.type_motor == 'turbojet engine' and self.count_turbojet_engine == 4 and passenger_capacity == 853:
                print(f"Your airplane is Airbus A380-800 and engine_thrust = {self.engine_thrust[1]}", "\n")
            else:
                raise Exception(MyException.not_name_airpalne())
        except Exception:
            print("Raised an exception", "\n")