#String é todo conteúdo que esteeja entre aspas simples ou duplas

print('Isso é uma string')
print("Isso também é uma string")

message = 'leonardo de oliveira costa'

print(message.title()) #torna toda inicial minuscula em maiúscula
print(message.upper()) #torna toda uma palavra maiuscula
print(message.lower()) #torna toda palavra minusculas

first_name = 'Leonardo'
last_name = 'Costa'

print(f'{first_name} {last_name}')

full_name = f'{first_name} {last_name}'
print(full_name)

#adicionar tabulação em texto: \t

print(f"\t{full_name}")

#adicionar quebras de linha em texto: \n

print('Languagens: \nPython\nJava\nC#\nDelphi')

#adicionar quebras de linha em texto com tabulação: \n\t

print('Languagens: \n\tPython\n\tJava\n\tC#\n\tDelphi')