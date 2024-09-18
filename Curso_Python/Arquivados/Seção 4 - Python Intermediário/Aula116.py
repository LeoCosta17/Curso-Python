def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

s1 = criar_saudacao('Boa noite')
s2 = criar_saudacao('Bom dia')

print(s1('Leo'))
print(s2('Brenda'))

name_list = [
    'João',
    'Maria',
    'José',
    'Jaiminho'
]

for name in name_list:
    print(s1(name))