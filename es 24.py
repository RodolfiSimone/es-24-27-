vote_A = int(input("numero voti per il primo candidato"))
vote_B = int(input("voti per il seconcdo"))
percentuale_A = (vote_A/(vote_A + vote_B))*100
percentuale_B = (vote_B/(vote_A + vote_B))*100
print("percentuale candidato A" , int(percentuale_A),"%","percentuale candidato B", int(percentuale_B), "%")
if vote_A > vote_B:
    print("il vincitore è il candidato A")
elif vote_B > vote_A:
    print("il vincitore è il candidato B")
else:
    print("pareggio")
