from math import prod
from math import fmod

def multiplication(*args):
    product = 0
    args = list(args)
    product = prod(args)
    return product

total_multi = multiplication(1, 2, 3)

print(f'Total da multiplicação: {total_multi}')

def odd_even(x):
    rest_div = fmod(x, 2)
    condition = rest_div == 0
    response = f'{x} é par!' if condition else f'{x} é impar!'
    return response

result = odd_even(3)

print(result)