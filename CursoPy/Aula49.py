n1 = input('valor de n1: ')
n2 = input('valor de n2: ')

try:
    int_n1 = int(n1)
    int_n2 = int(n2)
    print(f'Soma: {int_n1 + int_n2}')
except:
    print('Valores não correspondem a número!')