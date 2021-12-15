from itertools import chain, combinations
import time

def powerset(J):
    return chain.from_iterable(combinations(J, r) for r in range(len(J)+1))



start= time.time()

res = list(powerset([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))

"""
for r in res:
    print(list(r))
"""  
    
print("this took", time.time()-start)