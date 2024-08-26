s1 = set()

s1.add('Brenda')
s1.update(('Leonardo',))
s1.update('Leonardo')
print(s1)

s1.discard('e')

print(s1)