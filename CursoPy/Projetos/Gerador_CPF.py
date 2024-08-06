# Programa que cria quantos CPFs válidos forem solicitados pelo usuário
import random

# 1 - Os 9 digitos gerados são ordenadamente multiplicados
# pela sequência 10, 9, 8, 7, 6, 5, 4, 3, 2
# (o primeiro por 10, o segundo por 9, e assim sucessivamente)
# os produtos devem ser somados, e sua soma multiplicada por 10

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

multiplicador = 10
soma_digitos = 0

for digito in nove_digitos:
    soma_digitos += (int(digito) * multiplicador)
    multiplicador -= 1

# 2 - Nesta etapa é verificado o valor a ser gerado do primeiro digito
# Se o resto da divisão da multiplicação da soma dos produtos for menor ou igual a 9
# O valor do dígito será o próprio resto da divisão
# Caso for maior, será 0

multiplicacao_soma_digitos = soma_digitos * 10

resto_div = multiplicacao_soma_digitos % 11

primeiro_digito = resto_div if resto_div <= 9 else 0

# 3 - Com o primeiro dígito já gerado, ele é adicionado aos 9 primeiros, formando agora 10 dígitos

dez_digitos = nove_digitos + str(primeiro_digito)

# 4 - Para gerar o segundo dígito, é o mesmo processo do primeiro, porém
# são ordenadamente multiplicados pela sequência 11, 10, 9, 8, 7, 6, 5, 4, 3, 2
# (o primeiro por 11, o segundo por 10, e assim sucessivamente)

multiplicador = 11
soma_digitos = 0

for digito in dez_digitos:
    soma_digitos += (int(digito) * multiplicador)
    multiplicador -= 1
    
# 5 - Será realizada a mesma validação usada para gerar o primeiro dígito

multiplicacao_soma_digitos = soma_digitos * 10

resto_div = multiplicacao_soma_digitos % 11

segundo_digito = resto_div if resto_div <= 9 else 0

# 6 - Será adicionado o segunto digito aos outros 10 que compõem o CPF, formando o n° completo

cpf_gerado = dez_digitos + str(segundo_digito)

print(f'CPF gerado: {cpf_gerado}')