x = input('Primeiro valor: ')
y = input('Segundo valor: ')

int_x = int(x)
int_y = int(y)

if int_x > int_y:
    print('O primeiro valor é maior')
elif int_y > int_x:
    print('O segundo valor é maior')
else:
    print('Os valores são iguais!')
