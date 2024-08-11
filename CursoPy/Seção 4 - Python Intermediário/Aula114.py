from math import prod

def multiplication(*args):
    result = 0
    args = list(args)
    result = prod(args)
    return result


number_list = [2, 5]

def response(multiplication_result):
    print(f'Multiplication result: {multiplication_result}')

multiplication_result = multiplication(*number_list)

response(multiplication_result)