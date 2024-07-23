horario = int(input('Que horas são: '))

manha = horario >= 0 and horario <= 11
tarde = horario >= 12 and horario <= 17
noite = horario >= 18 and horario <= 23

if manha:
    print('Bom dia!')
elif tarde:
    print('Boa tarde!')
elif noite:
    print('Boa noite!')
else:
    print('Horário informado não é válido!')