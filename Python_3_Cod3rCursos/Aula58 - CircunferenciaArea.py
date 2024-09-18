"""Programa que realiza o cálculo da área de uma circunferência."""


#!python

if __name__ == '__main__':

    from math import pi
    from math import pow


    ERRO = '\033[91m]'
    NORMAL = '\033[00m]'
    
    def calculo_area(raio):
        """Realiza o cálculo da área e retorna o valor do mesmo."""
        area = pi * pow(raio, 2)
        return f'{area:.2f}'

    while True:
        try:
            raio = float(input('Informe o raio: '))
            
            area = calculo_area(raio)

            print(area)
            break
            
        except ValueError as error:
            print(f'{ERRO}Valor incorreto ou não informado!{NORMAL}\n{error}')
            