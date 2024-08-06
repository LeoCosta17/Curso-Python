def soma(x=None, y=None, z=None):
    total_soma = 0
    if x is not None:
        total_soma += x
    if y is not None:
        total_soma += y
    if z is not None:
        total_soma += z
    print(f'{x=} {y=} {z=}\nSoma: {total_soma}')

soma(1, 2)