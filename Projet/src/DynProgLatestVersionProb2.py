from itertools import combinations
from dataExtractor import getData2
import time


#Cette fonction permetra de mettre un element j d'une séquance J à la fin de cette séquance
def putLast(S,J,j):
    J2 = J[:] 
    J2.remove(j)
    J2.append(j)
#on enlève j de sa position et on le met à la fin
    return J2

#cette fonction va retourner 1 si j qui est à l fin est enretard et 0 sinon
def calculerFonctionObjective(S,J,j):
    if S == 1:
        if data[j][0]>data[j][1]:
            T = 1 
            E = 0
        elif data[j][0]>data[j][1]:
            T = 0
            E = 0
        else:
            T = 0
            E = 1
        
        return (data[j][2]*E) + (data[j][3]*T)
        
    if S==2:
        r1 = calculerFonctionObjective(1,J[:1],J[0])
        if data[J[0]][0] + data[J[1]][0] > data[J[1]][1]:
            T=1
            E=0
        elif data[J[0]][0] + data[J[1]][0] == data[J[1]][1]:
            T = 0
            E = 0
        else:
            T=0
            E=1
        r2 = (data[J[1]][2]*E) + (data[J[1]][3]*T)
        return r1+r2
    
    
    if res[tuple(J[:S-1])][0] + data[j][0] > data[j][1]:
        T=1
        E=0
    elif res[tuple(J[:S-1])][0] + data[j][0]== data[j][1]:
        T=0
        E=0
    else:
        T=0
        E=1
    
    return (data[j][2]*E) + (data[j][3]*T)        
    

def F(S,J):

#C'est la fonction récursive

#si la taille est 1 alors directement remplir sa case dans res avec pj, si j est en retard ou non, la séquance 
#n'est que [j] et j est à la fin
    if S == 1: 
        res[tuple(J)]=[ data[J[0]][0], calculerFonctionObjective(S, J, J[0]), J, J[0]]
        return 
    
#si la taille est deux on teste les deux cas possibles et on prend leur min    
    if S == 2:
        tmp = []
        case1 = putLast(S, J, J[0])
        case2 = J.copy()
        tmp.append(calculerFonctionObjective(S, case1, J[0]) + res[tuple(case1[:S-1])][1])
        tmp.append(calculerFonctionObjective(S, case2, J[1]) + res[tuple(case2[:S-1])][1])
        finnished = data[J[0]][0] + data[J[1]][0]
        t=min(tmp)
        if tmp.index(t) == 0:
            seq = case1[:]
        else:
            seq = case2[:]
        
        last=J[tmp.index(t)]
        
        
        res[tuple(J)]= [finnished, t, seq, last]
        return 

#si la taille est >2 alors utiliser les résultats déjà calculer des sous séquances    
#et prendre leurs min
    
    finnished = res[tuple(J[:S-1])][0] + data[J[S-1]][0] 
    
    
    tmp = {}
    for i in range(S):
        previous = putLast(S,J,J[i])
        t=0
        if finnished > data[J[i]][1]:
           t=1
#dans tmp on ne garde qu'une seule occurence de chaque nombre de retard pour minimiser la consommation de la mémoire un peu         
        tmp[t + res[tuple(previous[:S-1])][1]]= previous
     
#prendre le min des retard
    t = min(tmp.keys())
#et prendre la séquance qui a donnée ce min
    seq = tmp[t]
    
    res[tuple(J)]=[ finnished, t, seq, seq[-1:-2:-1][0] ] 
# se sevenir de l'élément à la fin car on l'utilisera pour construire la séquance optimale
    return             

#initialiser res par la condition initiale qui est la séquance vide
res={
     tuple([]): [0,0,0,0]
     }


n=10

data=getData2("../instances/P2_n"+str(n)+".txt")



start = time.time()


J = [i for i in range(1,11)]
cpt = 0

for r in range(1,len(J)+1):
    if cpt<2:
        state=list(combinations(J, r))
        cpt+=1
        for subSet in state:
            F(len(subSet), list(subSet))
    else:
#Pour pouvoir aller vers n un peut plus grand que ce qu'on peut maintenat (23) on supprimera
#ce les sous liste de taille S-2 (S la taille des sous listes actuelle) pour libérer la RAM 
#mais cette technique ne permettera que d'avoir la valeur minimale (sans séquance) ce qui n'est pas intéressant
#Donc on le met dans une commentaire pour le retrouver après des raisons de tests seulement

#        keysToDelete = []
#        for key in res.keys():
#            if len(key) == r-2:
#                keysToDelete.append(key)
#        for key in keysToDelete:
#            del res[key]
        
        state=list(combinations(J, r))
        cpt=0
        for subSet in state:
            F(len(subSet), list(subSet))
        #keysToDelete.clear()

# conserver le résultat des taches
ress = res[tuple(J)]

#ici on va construire une séquance optimale
sequance = []

#prendre la liste des clés qui sont les sous liste de la liste des tâches
ks=list(res.keys())

#parcourir de fin vers le début

for k in ks[-1:-len(ks):-1]:
    if list(k) == J:
#pour chaque sous séquance prendre la tache qui doit être à la fin pour minimiser le retard        
        sequance.append(res[k][3])
# enlever cette tâche et refaire jusq'au construction de la séquance optimale
        prev = J.remove(res[k][3])
    else:
        if list(k) == prev:
            sequance.append(res[k][3])
            prev = prev.remove(res[k][3])

#renverser pour retrouver l'ordre début vers fin
sequance = sequance[-1::-1]
print("(une) Séquance optimale: ", sequance)
print("Valeur minimale : ", ress[1])
print("Temps de fin du séquance : ", ress[0])

print("This Took", time.time()-start)


