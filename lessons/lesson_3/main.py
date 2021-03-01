from pprint import pprint
from time import time
from functools import wraps

'''
Task # 1
'''


def square(numbers, degree):
    changed_numbers = []
    for num in numbers:
        changed_numbers.append(num ** degree)
    return changed_numbers


'''
Task # 2
'''


def even_numbers(num):
    return num % 2 == 0


def odd_numbers(num):
    return num % 2 != 0


def simple_numbers(num):
    divider = 2
    if num > 1:
        while divider ** 2 <= num and num % divider != 0:
            divider += 1
        return divider ** 2 > num


def choice_filter_func(numbers_int):
    print('Original list of int numbers:', numbers_int)
    tmp = input('Enter "even" or "odd", or "simple" for start type of filter: ')
    if tmp == 'even':
        print('List after even filter:', list(EVEN_FILTER))
    elif tmp == 'odd':
        print('List after odd filter:', list(ODD_FILTER))
    elif tmp == 'simple':
        print('List after simple filter:', list(SIMPLE_FILTER))


'''
Task # 3 
Example of number Fibonacci with runtime decorator.
Without bonus task.
'''


def time_call_any(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        print("res ", args, kwargs, " = ", res)
        time_taken = end - start
        print(f"time taken: {time_taken:.13f}")
        return res
    return wrapper


@time_call_any
def fib(pos):
    if pos == 0:
        return 0
    if pos in (1, 2):
        return 1
    return fib(pos - 1) + fib(pos - 2)


if __name__ == '__main__':
    print('--------------------Task #1 ----------------------------------')
    int_numbers = list(map(int, input('Enter integer numbers separated by a space = ').strip().split()))
    keyword = int(input('Enter integer degree = '))
    pprint(square(int_numbers, keyword))

    print()
    print('--------------------Task #2 ----------------------------------')
    integer_numbers = [6, -19, 0, 3, 4, -12, 8, 7, 1]
    EVEN_FILTER = filter(even_numbers, integer_numbers)
    ODD_FILTER = filter(odd_numbers, integer_numbers)
    SIMPLE_FILTER = filter(simple_numbers, integer_numbers)
    choice_filter_func(integer_numbers)

    print()
    print('--------------------Task #3 ----------------------------------')
    pos_fib = int(input('Enter position for number Fibonacci: '))
    fib(pos_fib)
