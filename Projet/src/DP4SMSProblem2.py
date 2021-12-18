from itertools import  combinations
import time


def putLast(S,J,j):
    J2 = J.copy()
    J2.remove(j)
    J2.append(j)
    
    return J2

def calculerFonctionObjective(S,J,j):
    if S == 1:
        if P[j]>D[j]:
            T = 1
            E = 0
        elif P[j]==D[j]:
            T = 0
            E = 0
        else:
            T = 0
            E = 1
        
        return (a[j]*E) + (b[j]*T)
        
    if S==2:
        r1 = calculerFonctionObjective(1,J[:1],J[0])
        if P[J[0]] + P[J[1]] > D[J[1]]:
            T=1
            E=0
        elif P[J[0]] + P[J[1]] == D[J[1]]:
            T = 0
            E = 0
        else:
            T=0
            E=1
        r2 = (a[J[1]]*E) + (b[J[1]]*T)
        return r1+r2
    
    
    if res[tuple(J[:S-1])]["finnished"] + P[j] > D[j]:
        T=1
        E=0
    elif res[tuple(J[:S-1])]["finnished"] + P[j]==D[j]:
        T=0
        E=0
    else:
        T=0
        E=1
    
    return (a[j]*E) + (b[j]*T)
        
    

def F(S,J):
    
    if S == 1:
        res[tuple(J)]={
                "finnished" : P[J[0]],
                "fctObj" : calculerFonctionObjective(S, J, J[0]),
                "seq": J
        }
        return 
    
    
    if S == 2:
        tmp = []
        case1 = putLast(S, J, J[0])
        case2 = J.copy()
        tmp.append(calculerFonctionObjective(S, case1, J[0]) + res[tuple(case1[:S-1])]["fctObj"])
        tmp.append(calculerFonctionObjective(S, case2, J[1]) + res[tuple(case2[:S-1])]["fctObj"])
        finnished = P[J[0]] + P[J[1]]
        t=min(tmp)
        seq = J.copy()
        last=J[tmp.index(t)]
        seq.remove(last)
        
        res[tuple(J)]={
                "finnished" : finnished,
                "fctObj" : t,
                "seq": seq,
                "last": last
        }
        return 
    
    finnished = res[tuple(J[:S-1])]["finnished"] + P[J[S-1]] 
    
    
    tmp = []
    for i in range(S):
        previous = putLast(S,J,J[i])
        t=0
        if finnished > D[J[i]]:
           t=1
         
        tmp.append(t + res[tuple(previous[:S-1])]["fctObj"])
    
    
    t = min(tmp)
    seq = J.copy()
    last=J[tmp.index(t)]
    seq.remove(last)
    
    
    res[tuple(J)]={
                "finnished" : finnished,
                "fctObj" : t,
                "seq": seq,
                "last": last
        }
    return             
 
res={
     tuple([]): {
                     "finnished" : 0,
                     "fctObj" : 0
                 }
     }

P={
   1:24,
   2:1, 
   3:47,
   4:48,
   5:4,
   6:23,
   7:41,
   8:18,
   9:19,
   10: 50
}

D={
   1:57,
   2:144, 
   3:46,
   4:214,
   5:162,
   6:96,
   7:219,
   8:235,
   9:74,
   10:184,
}

a={
   1:3,
   2:6, 
   3:5,
   4:9,
   5:9,
   6:2,
   7:3,
   8:5,
   9:7,
   10:6,
}

b={
   1:1,
   2:1, 
   3:6,
   4:2,
   5:1,
   6:3,
   7:4,
   8:4,
   9:1,
   10:4,
}


start = time.time()



cpt = 0

J=[1,2,3,4]


for r in range(1,len(J)+1):
    if cpt<2:
        state=list(combinations(J, r))
        cpt+=1
        for subSet in state:
            F(len(subSet), list(subSet))
    else:
        keysToDelete = []
        for key in res.keys():
            if len(key) == r-2:
                keysToDelete.append(key)
        for key in keysToDelete:
            del res[key]
        
        state=list(combinations(J, r))
        cpt=0
        for subSet in state:
            F(len(subSet), list(subSet))
    

print(res)



print("This Took", time.time()-start)
