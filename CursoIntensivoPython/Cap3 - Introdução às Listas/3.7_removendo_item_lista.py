guest_list = [
    'Abel Ferreira',
    'Felipão',
    'São Marcos',
    'Romário',
    'Rogério Ceni',
    'Weverton'
]

list_length = len(guest_list)
condition = list_length > 2 
removed_guest = ''

while condition:
    convidado_removido = guest_list.pop()
    print(f'Convidado removdo: {convidado_removido}')
    list_length -= 1
    condition = list_length > 2 

for index, name in enumerate(guest_list):
    print(f'Convidado: {index} - {name}')

del guest_list [0]
del guest_list [0]

print(guest_list)