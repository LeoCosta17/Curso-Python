try:    
    num_int = int(input('Informe um número: '))
    impar_par = num_int%2
    if impar_par == 0:
        print('É par1')
    else:
        print('É impar!')
except:
    print('Número não é inteiro!')