a = 'Leonardo'
b = 20
c = 2003

string = 'Nome:{nome} Idade:{idade} Ano Nasc.:{ano_nasci}'
string_format = string.format(
    nome = a, idade = b, ano_nasci = c
    )

print(string_format)