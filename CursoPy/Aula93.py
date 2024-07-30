frase = 'O rato roeu a roupa do rei de Roma'
frase_separada = frase.split()
frase_separada_ponto = frase.split('roupa')

print(frase_separada)
print(frase_separada_ponto)

for i, frase in enumerate (frase_separada):
    print(frase_separada[i])

string_join = '-'.join(frase_separada)
print(string_join)