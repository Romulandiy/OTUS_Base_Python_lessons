from pprint import pprint


class MyException(Exception):

    @staticmethod
    def output(fuel_tank, remaining_fuel_in_tank):
        pprint("Not enough fuel in tank")
        pprint(f"remaining_fuel_in_tank / fuel_tank = {remaining_fuel_in_tank}/{fuel_tank} ="
               f" {remaining_fuel_in_tank / fuel_tank}")
        print("motor is STOP", "\n")
