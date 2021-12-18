import time 
from StructuresDeVoisinnage import swap 
from StructuresDeVoisinnage import insert
from StructuresDeVoisinnage import twoOpt
from dataExtractor import getData 

def calculerNbRetard(x,data):
#On va calculer le nombre de taches en retard pour une séquance x
#inistialisations
    finnished = 0
    retard = 0

#pour chaque tache i on ajoute son pi (processing time) au temp
#de fin des tache qui la précède dans la séquance pour avoir ci (temp de fin)
# et si ce ci > di (due date) alors on incrémente le compteur des taches en retard 
#sinon rien faire

    for i in range(len(x)):
        finnished += data[x[i]][0]
        if finnished>data[x[i]][1]:
            retard +=1 
    
    return retard
        
     
def LocalSearchVND(lmax,Nl,x1,data):
     
#stocker le nombre de taches en retard pour la séqaunce x1 pour ne pas faire appel à la fonction chaque fois    
    retardx1 = calculerNbRetard(x1,data) 
    start = time.time() #se rappeler de quand on a commancé    
    while True:
#continuer à faire cela tant que la condition d'arret en ligne 43 n'est pas satisfaite        
        l=0 
# on commencepar la première structure de voisinnage 
        while l<lmax:
#faire tant qu'il y en a encore des structure de voisinage            
# shaking : générer aléatoirement une séquance dans la structure de voisinnage numéro l

            x2 = Nl[l](x1)            
            retardx2 = calculerNbRetard(x2, data)
            
            if retardx2 < retardx1: 
#si on a amélioration de la fonction objective alors alors prendre la séquance donnant l'amélioration au 
#lieu de la séquance courante                
                x1=x2[:]
                retardx1=retardx2
                l=0 # et revenir au première structure de voisinnage
            else:
                l+=1 # sinon conserver la même séquance et passer au structure de voisinnage suivante
         
        if time.time() - start > n*0.005: # si on dépasse un temps donné dans cette boucle alors arrêter (c'est la condition d'arrêt)            
        #if time.time() - start > 200 :             
            break
    return x1
 

def VNS(x,Nk,kmax,Nl,lmax,data):

# même démarche que VND    
    retardx = calculerNbRetard(x, data)
    start = time.time()
    stopCondition = False
    while not stopCondition:
        k=0
        
        while k<kmax:
            
# shaking : générer une séquance aléatoire à partir de la structure de voisinnage numéro k             
            x1 = Nk[k](x) 
#appliquer la recherche locale sur x1 
            
            x1 = LocalSearchVND(lmax, Nl, x1, data)
            retardx1 = calculerNbRetard(x1, data)
            if retardx1 < retardx:
# si la séquance résultante de VND améliore la fonction objective alors prendre cette séquance et retourner au première structure de voisinnage                 
                x=x1[:]
                retardx = retardx1
                k=0
            else:
#sinon continuer vers la structure de voisinnage suivante                
                k+=1
         
        if time.time() - start > n*0.005 : 
        #if time.time() - start > 200 : 
# après un temps déterminer sortir            
            stopCondition = True
    
    return x

    
# stocker les structures de voisinnage (fonctions) dans les deux tables Nk et Nl    
Nk= [twoOpt,insert, swap]
kmax = len(Nk)
Nl= [twoOpt,insert,swap]
lmax = len(Nl)

#extraire les données du fichier

n=500

data=getData("../instances/P1_n"+str(n)+".txt")

#initialisation de la séquance de démmarage


x=[ i+1 for i in range(n) ]


started = time.time()

#Appliquer l'algo de choix de la séquance de démmarage
x=LocalSearchVND(lmax, Nl, x, data)

#appliquer VNS pour avoir la séquance optimale
x=VNS(x, Nk, kmax, Nl,lmax, data)


print(x)
print(calculerNbRetard(x, data)) 

print("finnished", time.time()-started)




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    