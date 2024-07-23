idade = input('Qual sua idade?')
int_idade = int(idade)

if(int_idade < 18):
    print('Menor de idade')
elif(int_idade >= 18 and int_idade<=50):
    print('Maior de idade')
else:
    print('Defunto!')