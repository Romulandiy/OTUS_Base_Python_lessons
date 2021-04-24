from lessons.lesson_8.Engine import Engine
from lessons.lesson_8.PassengerCar import PassengerCar


car_example_1 = PassengerCar(weight=1300,
                             carrying_capacity=556,
                             number_of_wheels=4,
                             fuel_tank_volume=65,
                             fuel_remaining_in_tank=23)

engine_1 = Engine(maximum_engine_speed=6800,
                  number_of_pistons=6,
                  liter=3.2)

car_example_2 = PassengerCar(weight=1300,
                             carrying_capacity=556,
                             number_of_wheels=4,
                             fuel_tank_volume=65,
                             fuel_remaining_in_tank=2)

engine_2 = Engine(maximum_engine_speed=5500,
                  number_of_pistons=4,
                  liter=1.4)


if __name__ == '__main__':
    '''
    Example # 1 
    Methods of classes PassengerCar and Engine
    '''
    car_example_1.start_motor(fuel_tank=car_example_1.fuel_tank_volume,
                              remaining_fuel_in_tank=car_example_1.fuel_remaining_in_tank)
    car_example_1.make_sound()
    car_example_1.go(engine_1)
    car_example_1.go(engine_2)

    '''
    Example # 2 
    Methods of classes PassengerCar and Engine
    '''
    car_example_2.start_motor(fuel_tank=car_example_2.fuel_tank_volume,
                              remaining_fuel_in_tank=car_example_2.fuel_remaining_in_tank)
