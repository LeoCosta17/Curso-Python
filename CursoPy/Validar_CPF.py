cpf = input('Informe o CPF: ')
cpf_sem_ponto = cpf.replace('.', '')
cpf_limpo = cpf_sem_ponto.replace('-', '')

nove_digitos = cpf_limpo[:9]

multiplicador = 10
soma_digitos = 0

for digito in nove_digitos:
    soma_digitos += (int(digito) * multiplicador)
    multiplicador -= 1

multiplicacao_soma_digitos = soma_digitos * 10

resto_div = multiplicacao_soma_digitos % 11

primeiro_digito = resto_div if resto_div <= 9 else 0

dez_digitos = nove_digitos + str(primeiro_digito)

multiplicador = 11
soma_digitos = 0

for digito in dez_digitos:
    soma_digitos += (int(digito) * multiplicador)
    multiplicador -= 1
    
multiplicacao_soma_digitos = soma_digitos * 10

resto_div = multiplicacao_soma_digitos % 11

segundo_digito = resto_div if resto_div <= 9 else 0

cpf_validado = dez_digitos + str(segundo_digito)

validacao = 'CPF informado é válido' if cpf_validado == cpf_limpo else 'CPF inválido'
print(f'CPF informado: {cpf_limpo}\nCPF validado: {cpf_validado}\n{validacao}')