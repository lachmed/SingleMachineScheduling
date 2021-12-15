from random import random


def insert(liste):
    l = len(liste)
    
    i = int(random()*(l-1))
    j=i
    
    while j==i:
        j = int(random()*(l-1))
    
#choisir un élément aléatoirement le mettre dans une autre position aléatoire
    
    tmp = liste.copy()
    tmp.remove(liste[i])
    tmp.insert(j,liste[i])
    
    return tmp


print(insert([1,7,8,9,10,5,3,2,4,6]))