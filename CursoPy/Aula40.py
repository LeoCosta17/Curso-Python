print('Para comprar, necessário ter mais de 18 anos, e renda maior que R$3.000,00')
idade = input('Idade: ')
renda = input('Renda: ')
int_idade = int(idade)
float_renda = float(renda)

if int_idade > 18 and float_renda > 3000:
    print('Compra liberada!')
else:
    print('Compra negada!')