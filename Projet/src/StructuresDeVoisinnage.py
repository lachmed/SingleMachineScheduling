from random import random

def twoOpt(liste):
    l = len(liste)

    i = int(random()*(l-3))
# ici l-3 car sinon (l-2 jusiqu'à l-1) on tombera dans une boucle infinie
#lorsqu'on veut trouver j
    j= (i*int(random()*(l)))%(l)
    
    if i>j:
        tmp = i
        i=j
        j=tmp
    
    tmp = liste[:]
#Diviser la liste en trois parties
    part1= tmp[:i]
    part2= tmp[i:j+1]
    part3= tmp[j+1:]
#renverser l'ordre de la partie au milieu
    part2 = part2[-1::-1]

#reconstruire la liste pour un voisin dans 2-opt    
    return part1+part2+part3

def insert(liste):
    l = len(liste)
    
    i = int(random()*(l-1))
    j=i
    
    while j==i:
        j = int(random()*(l-1))
    
#choisir un élément aléatoirement le mettre dans une autre position aléatoire
    
    tmp = liste[:]
    tmp.remove(liste[i])
    tmp.insert(j,liste[i])
    
    return tmp


def swap(liste):
    l = len(liste)
    i = int(random()*(l-1))
    j=i
    
    while j==i:
        j = int(random()*(l-1))

#choisir deux éléments aléatoirement et echanger leurs positions
    tmp = liste[:]
    tmp.remove(liste[i])
    tmp.remove(liste[j])
    tmp.insert(i,liste[j])
    tmp.insert(j,liste[i])
    
    return tmp




    	
