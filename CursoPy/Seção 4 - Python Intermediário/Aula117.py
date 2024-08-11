def duplicador(d):
    def duplicar(x):
        return x * d
    return duplicar

def triplicador(d):
    def triplicar(x):
        return x * d
    return triplicar

def quadruplicador(d):
    def quadruplicar(x):
        return x * d
    return quadruplicar

new_duplicador = duplicador(2)
new_triplicador = triplicador(3)
new_quadruplicador = quadruplicador(4)

numero_receber = 5

print(new_duplicador(numero_receber))
print(new_triplicador(numero_receber))
print(new_quadruplicador(numero_receber))