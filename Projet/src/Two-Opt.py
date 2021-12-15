from random import random

def twoOpt(liste):
    l = len(liste)

    i = int(random()*(l-3))
# ici l-3 car sinon (l-2 jusiqu'à l-1) on tombera dans une boucle infinie
#lorsqu'on veut trouver j
    j=i
    
    while  j<=i:
        j = int(random()*(l-1))


    
    tmp = liste.copy()
#Diviser la liste en trois parties
    part1= tmp[:i]
    part2= tmp[i:j+1]
    part3= tmp[j+1:]
#renverser l'ordre de la partie au milieu
    part2.reverse()

#reconstruire la liste pour un voisin dans 2-opt    
    return part1+part2+part3



print(twoOpt([1,7,8,9,10,5,3,2,4,6]))



    
    
    
    
