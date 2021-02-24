from pprint import pprint, pformat


def square(n, degree):
    changed_n = []
    for i in n:
        changed_n.append(i ** degree)
    return changed_n


n = list(map(int, input('Enter integer numbers separated by a space = ').strip().split()))
keyword = int(input('Enter integer degree = '))
pprint(square(n, keyword))
