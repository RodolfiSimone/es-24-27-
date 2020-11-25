candidato_A = input("nome del primo candidato")
punteggio_A = int(input("punteggio del primo candidato"))
candidato_B = input("nome del secondo candidato")
punteggio_B = int(input("punteggio del secondo candidato"))
nomi = [candidato_A, candidato_B]
nomi.sort()
punteggi = [punteggio_A, punteggio_B]
punteggi.sort()
punteggi.reverse()
print (nomi, punteggi)