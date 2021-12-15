import time

def inverse(liste):
    return liste[-1::-1]

def cycle(liste):
    tmpliste = liste[:]
    tmp= tmpliste[0]
    tmpliste.remove(tmp)
    tmpliste.append(tmp)
    return tmpliste


def findStarters(liste):
    starters = []
    if len(liste) <=3:
        starters.append(liste)
        return starters
    
    fixed = []
    fixed.append(liste[0])
    liste.remove(fixed[0])
    permutations = findPermutations(liste)
    
    equiv = []
    for p in permutations:
        tmp=fixed+p
        if (tmp) not in equiv:
            starters.append(tmp)
            tmp2 = cycle(tmp)
            tmp2 = inverse(tmp2)
            equiv.append(tmp2)
        else:
            continue
        
    return starters
    

def findPermutations(liste):
    starters = findStarters(liste)
    permutations = []
    
    for s in starters:
        cycles=[]
        for i in range(len(s)-1):
            cycles.append(cycle(s))
        permutations.append(s)
        permutations.append(inverse(s))
        for c in cycles:
            permutations.append(c)
            permutations.append(inverse(c))

    return permutations


start = time.time()

b = findPermutations([1,2,3,4,5,6,7,8,9,10])

print("this took", time.time()-start)
print("Generated", len(b))


