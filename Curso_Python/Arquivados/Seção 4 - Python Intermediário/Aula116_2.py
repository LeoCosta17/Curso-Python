def multiplicador(m):
    def multiplicar(x):
        return x * m
    return multiplicar

multiplicar_por4 = multiplicador(4)
multiplicar_por10 = multiplicador(10)

print(multiplicar_por4(4))
print(multiplicar_por10(4))