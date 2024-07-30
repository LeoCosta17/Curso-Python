salas = [
    #0       #1       #2   
    ['Joao', 'Maria', 'Raquel'],#0

    ['Fernando', 'Isaque', 'Luiz'],

    ['Joana', 'Roberta', 'Laura']
]

for i, sala in enumerate (salas):
    print(f'Sala - {i}')
    for aluno in sala:
        print(f'Aluno: {aluno}')