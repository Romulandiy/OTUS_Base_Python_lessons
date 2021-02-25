from pprint import pprint, pformat

# def square(n, degree):
#     changed_n = []
#     for i in n:
#         changed_n.append(i ** degree)
#     return changed_n
#
#
# n = list(map(int, input('Enter integer numbers separated by a space = ').strip().split()))
# keyword = int(input('Enter integer degree = '))
# pprint(square(n, keyword))

int_numbers = [6, -19, 0, 3, 4, -12, 8, 7, 1]


def even_numbers(num):
    if num % 2 == 0:
        return True
    else:
        return False


def odd_numbers(num):
    if num % 2 != 0:
        return True
    else:
        return False


def simple_numbers(num):
    divider = 2
    if num > 1:
        while divider ** 2 <= num and num % divider != 0:
            divider += 1
        return divider ** 2 > num


even_filter = filter(even_numbers, int_numbers)
print('List after even filter:', list(even_filter))

odd_filter = filter(odd_numbers, int_numbers)
print('List after odd filter:', list(odd_filter))

simple_filter = filter(simple_numbers, int_numbers)
print('List after simple filter:', list(simple_filter))

