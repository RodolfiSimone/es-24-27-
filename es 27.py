somma_macchine = 0
while True:
    macchine = int(input("numero macchine oggi "))
    if macchine == 0:
        break
    somma_macchine = somma_macchine + macchine

print ("il numero di macchine transitate in questo periodo di tempo è di ", somma_macchine)