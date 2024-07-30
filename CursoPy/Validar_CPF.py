# Programa que válida o CPF, de acordo com cálculo feito pelo Governo Federal

# 1 - Usuário insere o CPF
cpf = input('Informe o CPF: ')

# 2 - CPF será limpo, removido os '.' (pontos) e '-' (traços)
cpf_sem_ponto = cpf.replace('.', '')
cpf_limpo = cpf_sem_ponto.replace('-', '')

# 3 - Separo os 9 primeiros digitos do CPF
# e são ordenadamente multiplicados pela sequência 10, 9, 8, 7, 6, 5, 4, 3, 2
# (o primeiro por 10, o segundo por 9, e assim sucessivamente)
# os produtos devem ser somados, e sua soma multiplicada por 10

nove_digitos = cpf_limpo[:9]

multiplicador = 10
soma_digitos = 0

for digito in nove_digitos:
    soma_digitos += (int(digito) * multiplicador)
    multiplicador -= 1

# 4- Nesta etapa é verificado o valor a ser gerado do primeiro digito
# Se o resto da divisão da multiplicação da soma dos produtos for menor ou igual a 9
# O valor do dígito será o próprio resto da divisão
# Caso for maior, será 0

multiplicacao_soma_digitos = soma_digitos * 10

resto_div = multiplicacao_soma_digitos % 11

primeiro_digito = resto_div if resto_div <= 9 else 0

# 5 - Com o primeiro dígito já gerado, ele é adicionado aos 9 primeiros, formando agora 10 dígitos

dez_digitos = nove_digitos + str(primeiro_digito)

# 6 - Para gerar o segundo dígito, é o mesmo processo do primeiro, porém
# são ordenadamente multiplicados pela sequência 11, 10, 9, 8, 7, 6, 5, 4, 3, 2
# (o primeiro por 11, o segundo por 10, e assim sucessivamente)

multiplicador = 11
soma_digitos = 0

for digito in dez_digitos:
    soma_digitos += (int(digito) * multiplicador)
    multiplicador -= 1
    
# 7 - Será realizada a mesma validação usada para gerar o primeiro dígito

multiplicacao_soma_digitos = soma_digitos * 10

resto_div = multiplicacao_soma_digitos % 11

segundo_digito = resto_div if resto_div <= 9 else 0

# 8 - Será adicionado o segunto digito aos outros 10 que compõem o CPF, formando o n° completo

cpf_validado = dez_digitos + str(segundo_digito)

# 9 - Caso o CPF formado pela validação for o mesmo que o informado, será considerado
# um CPF válido, caso for diferente, será inválido.

validacao = 'CPF informado é válido' if cpf_validado == cpf_limpo else 'CPF inválido'
print(f'CPF informado: {cpf_limpo}\nCPF validado: {cpf_validado}\n{validacao}')