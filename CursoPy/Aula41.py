print('--Vaga Idoso/PCD')
idoso = input('idade: ')
pcd = input('PCD: [S/N]')

int_idoso = int(idoso)

if int_idoso >= 70 or pcd == 'S':
    print('Você tem direito à vaga de PCD!')
else:
    print('Você não tem direito!')