from lessons.lesson_8.Engine import Engine
from lessons.lesson_8.PassengerCar import PassengerCar
from lessons.lesson_8.Sailboat import Sailboat


# Example # 1 ----------------------------------------
car_example_1 = PassengerCar(weight=1300,
                             carrying_capacity=556,
                             number_of_wheels=4,
                             fuel_tank_volume=65,
                             fuel_remaining_in_tank=23)

engine_1 = Engine(maximum_engine_speed=6800,
                  number_of_pistons=6,
                  liter=3.2)


# Example # 2 ----------------------------------------
car_example_2 = PassengerCar(weight=1300,
                             carrying_capacity=556,
                             number_of_wheels=4,
                             fuel_tank_volume=65,
                             fuel_remaining_in_tank=2)

engine_2 = Engine(maximum_engine_speed=5500,
                  number_of_pistons=4,
                  liter=1.4)


# Example # 3 ----------------------------------------
sailboat_example_3 = Sailboat(carrying_capacity=3200, weight=7300, sail_area=690, mast_height=10, displacement=23500)




if __name__ == '__main__':
    '''
    Example # 1 
    Methods of classes PassengerCar, Engine and MyException
    '''
    print('-------Example # 1--------')
    car_example_1.start_motor(fuel_tank=car_example_1.fuel_tank_volume, remaining_fuel_in_tank=car_example_1.fuel_remaining_in_tank)
    car_example_1.make_sound()
    car_example_1.go(engine_1)


    '''
    Example # 2 
    Methods of classes PassengerCar, Engine and MyException
    '''
    print('-------Example # 2--------')
    car_example_2.start_motor(fuel_tank=car_example_2.fuel_tank_volume, remaining_fuel_in_tank=car_example_2.fuel_remaining_in_tank)
    car_example_2.go(engine_2)


    '''
    Example # 3 
    Methods of classes Sailboat, Engine and MyException
    '''
    print('-------Example # 3--------')
    sailboat_example_3.make_sound()