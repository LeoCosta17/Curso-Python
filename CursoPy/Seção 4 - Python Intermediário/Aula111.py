def soma(*args):
    soma = 0
    for num in args:
        soma += num
    return soma

total_soma = soma(1 , 40, 15)

print(f'Total da soma: {total_soma}')