from pprint import pprint


class MyException:

    @staticmethod
    def output(fuel_tank, remaining_fuel_in_tank):
        pprint("Not enough fuel in tank")
        pprint(f"remaining_fuel_in_tank / fuel_tank = {remaining_fuel_in_tank}/{fuel_tank} ="
               f" {remaining_fuel_in_tank / fuel_tank}")
        print("motor is STOP", "\n")

    @staticmethod
    def max_passengers():
        print("You can take on board only 2 passengers")

    @staticmethod
    def not_name_airpalne():
        print("You have an unknown plane ")
