string = 'Leon ardo'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        print('String com espaços')
        break

    print(letra)
    i+=1
else:
    print('String sem espaços')