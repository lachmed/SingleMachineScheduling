from random import random


def swap(liste):
    l = len(liste)
    i = int(random()*(l-1))
    j=i
    
    while j==i:
        j = int(random()*(l-1))

#choisir deux éléments aléatoirement et echanger leurs positions
    tmp = liste.copy()
    tmp.remove(liste[i])
    tmp.remove(liste[j])
    tmp.insert(i,liste[j])
    tmp.insert(j,liste[i])
    
    return tmp
    


print(swap([1,7,8,9,10,5,3,2,4,6]))
