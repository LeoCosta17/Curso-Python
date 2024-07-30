tupla = (10, 20, 30)
lista = ['Joao', 'Maria', 'José']
string = 'Python'

# cada variável individual recebe um valor da sequência

a, b, c = tupla
d, e, f = lista
g, h, i, j, k, l = string

print(a, b, c)
print(d, e, f)
print(g, h, i, j, k, l)

# Operador * pode ser usado para agrupar valores restantes de uma lista (útil) quando
# não se sabe quantos elementos uma sequência terá

nums_int = [0,1,2,3,4,5,6,7,8,9,10]

first_num, second_num, *rest = nums_int

print(f'{first_num}\n{second_num}\n{rest}')

# Ou então, desempacotar todo conteudo

print(*nums_int, sep='\n')