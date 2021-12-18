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
    if S==2:
        t=0
        if P[J[0]] > D[J[0]]:
            t+=1
        if P[J[0]] + P[J[1]] > D[J[1]]:
            t+=1
        return t
    
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
    
    
    if S == 2:
        tmp = []
        case1 = putLast(S, J, J[0])
        case2 = J.copy()
        tmp.append(calculateTardiness(S, case1, J[0]) + res[tuple(case1[:S-1])]["tardiness"])
        tmp.append(calculateTardiness(S, case2, J[1]) + res[tuple(case2[:S-1])]["tardiness"])
        finnished = P[J[0]] + P[J[1]]
        t=min(tmp)
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
    
    finnished = res[tuple(J[:S-1])]["finnished"] + P[J[S-1]] 
    
    
    tmp = []
    for i in range(S):
        previous = putLast(S,J,J[i])
        t=0
        if finnished > D[J[i]]:
           t=1
         
        tmp.append(t + res[tuple(previous[:S-1])]["tardiness"])
    
    
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
   10: 50,
   11:12,
   12:30,
   13:15,
   14:60,
   15:57,
   16:144, 
   17:46,
   18:214,
   19:162,
   20:96,
   21:219,
   22:235,
   23:74,
   24:184,
   25:14,
   26:36,
   27:9,
   28:38
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
   11:14,
   12:36,
   13:9,
   14:38,
   15:24,
   16:1, 
   17:48,
   18:214,
   19:50,
   20:96,
   21:219,
   22:235,
   23:74,
   24:184,
   25:302,
   26:36,
   27:60,
   28:38
}


start = time.time()

subSets = list(powerset([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]))

subSets.remove(())

for J in subSets:
    J=list(J)
    F(len(J),J)


print(res)


print("This Took", time.time()-start)
