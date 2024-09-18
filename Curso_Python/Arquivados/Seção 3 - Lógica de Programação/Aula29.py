altura = 1.85
peso = 78
imc = peso / (altura ** 2)

print(imc)

if imc < 21.9:
    print('Baixo peso')
elif 22 <= imc <= 27:
    print('Peso normal')
elif 27.1 <= imc <= 30:
    print('Sobrepeso')
else:
    print('Obesidade')