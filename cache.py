from functools import cache
import sys


sys.setrecursionlimit(20000)
sys.set_int_max_str_digits(10000)

@cache
def srandicka(n):
    if n == 1 or n == 2:
        return n
    else:
        return srandicka(n - 1) + srandicka(n - 2)


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print(srandicka(1747))
print(factorial(1698))
