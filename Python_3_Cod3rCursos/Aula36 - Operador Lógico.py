trabalho_terca = False

trabalho_quinta = False

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_quinta != trabalho_terca
mais_saudavel = not sorvete

print(tv_50)
print(tv_32)
print(sorvete)
print(mais_saudavel)