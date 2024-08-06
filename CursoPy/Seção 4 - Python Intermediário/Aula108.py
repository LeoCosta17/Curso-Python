def soma(x, y):
    soma_total = x + y            #Escopo da função
    print(f'Soma: {soma_total}')

#print(soma_total)   # Variável dentro do escopo da função
                    # Não consegue ser acessado fora do escopo da função 'soma'


multi_total = 0 # Variável definida fora do escopo da função

def multi(x, y):
    global multi_total # Variável definida anteriormente 
    multi_total= x * y            #Escopo da função modifica a variável global, com novo valor
    print(f'Soma: {multi_total}')

multi(10,2)
print(multi_total)