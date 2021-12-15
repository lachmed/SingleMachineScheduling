from itertools import chain, combinations
import time

def powerset(J):
    return chain.from_iterable(combinations(J, r) for r in range(len(J)+1))

def putLast(S,J,j):
    J2 = J.copy()
    J2.remove(j)
    J2.append(j)
    
    return J2

def calculateTardiness(S,J,j):
    if S == 1:
        if P[j]>D[j]:
            return 1
        else:
            return 0
        
    if res[tuple(J[:S-1])]["finnished"] + P[j] > D[j]:
        return 1
    else:
        return 0
        
    

def F(S,J):
    
    if S == 1:
        res[tuple(J)]={
                "finnished" : P[J[0]],
                "tardiness" : calculateTardiness(S, J, J[0]),
                "seq": J
        }
        return 
    
    
    finnished = 0
    for j in J:
        finnished+=P[j]
    
    tmp = []
    for i in range(S):
        previous = J.copy()
        previous.remove(J[i])
        tmp.append(calculateTardiness(S,putLast(S,J,J[i]), j) + res[tuple(previous)]["tardiness"])
    
    t = min(tmp)
    seq = J.copy()
    last=J[tmp.index(t)]
    seq.remove(last)
    
    
    res[tuple(J)]={
                "finnished" : finnished,
                "tardiness" : t,
                "seq": seq,
                "last": last
        }
    return             
        

res={
     tuple([]): {
                     "Finnished" : 0,
                     "Tardiness" : 0
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
   10:184  
}


start = time.time()

subSets = list(powerset([1,2,3,4,5,6,7,8,9,10]))

subSets.remove(())

for J in subSets:
    J=list(J)
    F(len(J),J)


print(res)


print("This Took", time.time()-start)