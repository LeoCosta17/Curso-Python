message = 'Teste de espaço branco   '
print(message)
#rstrip remove espaços em brancos a direita do conteúdo
#Entretanto, para remover de forma definitiva, é necessário associar o valor removido a variável
message = message.rstrip()
print(message)

#lstrip remove espaços em branco a esquerda do conteúdo
message_2 = '   teste'
message_2 = message_2.lstrip()
print(message_2)

message_3 = '   teste   '
message_3 = message_3.strip()
print(message_3)

#remoção de prefixo
string_prefixo = 'https:\\novinhas_safadinhas.com'
print(string_prefixo)
string_sem_prefixo = string_prefixo.removeprefix('https:\\')
print(string_sem_prefixo)

python_file = 'python.txt'
python_file = python_file.removesuffix('.txt')
print(python_file)