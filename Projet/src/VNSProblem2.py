import time
from StructuresDeVoisinnage import swap 
from StructuresDeVoisinnage import insert
from StructuresDeVoisinnage import twoOpt
from dataExtractor import getData2

def calculerFonctionObjective(x,data):
#On va calculer le nombre de taches en retard pour une séquance x
#inistialisations
    finnished = 0
    T = 0
    E = 0
    
    res = 0
    
#pour chaque tache i on ajoute son pi (processing time) au temp
#de fin des tache qui la précède dans la séquance pour avoir ci (temp de fin)
# et si ce ci > di (due date) alors on incrémente le compteur des taches en retard 
#sinon rien faire

    for i in range(len(x)):
        
        finnished += data[x[i]][0]
        
        if finnished>data[x[i]][1]:
            T = 1 
            E = 0
        elif finnished==data[x[i]][1]:
            T= 0
            E= 0
        else:
            T = 0 
            E = 1
        
        res += (data[x[i]][2] * E) + (data[x[i]][3] * T)
    
    return res
        
    


def LocalSearchVND(lmax,Nl,x1,data):
     
    dejaTrouve = []
#stocker le nombre de taches en retard pour la séqaunce x1 pour ne pas faire appel à la fonction chaque fois    
    retardx1 = calculerFonctionObjective(x1,data) 
    start = time.time() #se rappeler de quand on a commancé    
    while True:
#continuer à faire cela tant que la condition d'arret en ligne 43 n'est pas satisfaite        
        l=0 
# on commencepar la première structure de voisinnage 
        NbEtirations = 0       
        while l<lmax:
#faire tant qu'il y en a encore des structure de voisinage            
# shaking : générer aléatoirement une séquance dans la structure de voisinnage numéro l
            NbEtirations +=1
            
            tmp = Nl[l](x1)
            NbEtirations1=0
            while tmp in dejaTrouve:
                tmp = Nl[l](x1)
                NbEtirations1+=1
                if NbEtirations1 > 3:
                    break
            dejaTrouve.append(tmp)
            x2=tmp 
            if calculerFonctionObjective(x2, data) < retardx1: 
#si on a amélioration de la fonction objective alors alors prendre la séquance donnant l'amélioration au 
#lieu de la séquance courante                
                x1=x2
                l=0 # et revenir au première structure de voisinnage
            else:
                l+=1 # sinon conserver la même séquance et passer au structure de voisinnage suivante
            
            if NbEtirations > 19:
                break
                
        if time.time() - start > 60: # si on dépasse un temps donné dans cette boucle alors arrêter (c'est la condition d'arrêt)            
            break
    print("Out of VND")
    return x1
 

def VNS(x,Nk,kmax,Nl,lmax,data):

# même démarche que VND    
    retardx = calculerFonctionObjective(x, data)
    start = time.time()
    stopCondition = False
    while not stopCondition:
        k=0
        dejaTrouve = []
        NbEtirations = 0
        while k<kmax:
            NbEtirations +=1
# shaking : générer une séquance aléatoire à partir de la structure de voisinnage numéro k             
            x1 = Nk[k](x) 
            NbEtirations2 = 0
            while x1 in dejaTrouve:
                x1 = Nk[k](x)
                NbEtirations2+=1
                if NbEtirations2 > 3:
                    break
            dejaTrouve.append(x1)
#appliquer la recherche locale sur x1 
            
            x1 = LocalSearchVND(lmax, Nl, x1, data)
        
            if calculerFonctionObjective(x1, data)< retardx:
# si la séquance résultante de VND améliore la fonction objective alors prendre cette séquance et retourner au première structure de voisinnage                 
                x=x1
                k=0
            else:
#sinon continuer vers la structure de voisinnage suivante                
                k+=1
            print("here k",k)
            print("here nb",NbEtirations)
            
            if NbEtirations > 19: 
# après un temps déterminer sortir                
                break
            
        print(time.time() - start)
        if time.time() - start > 1800 : 
# après un temps déterminer sortir            
            stopCondition = True
    
    return x

    
# stocker les structures de voisinnage (fonctions) dans les deux tables Nk et Nl    
Nk= [ twoOpt,insert, swap]
kmax = len(Nk)
Nl= [ twoOpt, swap, insert ]
lmax = len(Nl)

#extraire les données du fichier
 
data=getData2("../instances/P2_n10.txt")

#initialisation de la séquance de démmarage

#TODO : Appliquer l'algo de choix de la séquance de démmarage
x=[ i+1 for i in range(10) ]


started = time.time()
x=LocalSearchVND(lmax, Nl, x, data)
print("finnished", time.time()-started)
#appliquer VNS pour avoir la séquance optimale
x=VNS(x, Nk, kmax, Nl, lmax, data)

print(x)
print(calculerFonctionObjective(x, data))




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    