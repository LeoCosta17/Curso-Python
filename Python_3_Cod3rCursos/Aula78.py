def faixa_etaria(idade):
    if 0 < idade < 18:
        return 'Menor de idade'
    elif idade in range(18, 30):
        return 'Jovem'
    elif idade in range(30, 50):
        return 'Adulto'
    
print(faixa_etaria(17))