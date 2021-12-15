# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 10:17:23 2021

@author: hp
"""

def calculateTardiness(liste,res,P,D):
    
    if len(liste) == 1:
        res[tuple(liste)]= {
                "finished": P[liste[0]],
                "tardiness": 0
                }
        return 
    
    if len(liste)==2:
        if P[liste[0]] + P[liste[1]] > D[liste[1]]:
            res[tuple(liste)]= {
                "finished": P[liste[0]] + P[liste[1]],
                "tardiness": 1
                }
        else:
            res[tuple(liste)]= {
                "finished": P[liste[0]] + P[liste[1]],
                "tardiness": 0
                }
        return

    
    l = len(liste)
    if tuple(liste[:l-1]) in res.keys():
        if res[tuple(liste[:l-1])]["finished"] + P[liste[l-1]] > D[liste[l-1]] :
            res[tuple(liste)]= {
                "finished": res[tuple(liste[:l-1])]["finished"] + P[liste[l-1]],
                "tardiness": res[tuple(liste[:l-1])]["tardiness"] + 1
                }
        else:
            res[tuple(liste)]= {
                "finished": res[tuple(liste[:l-1])]["finished"] + P[liste[l-1]],
                "tardiness": res[tuple(liste[:l-1])]["tardiness"]
                }
    else:
        calculateTardiness(liste[:l-1])
        if res[tuple(liste[:l-1])]["finished"] + P[liste[l-1]] > D[liste[l-1]] :
            res[tuple(liste)]= {
                "finished": res[tuple(liste[:l-1])]["finished"] + P[liste[l-1]],
                "tardiness": res[tuple(liste[:l-1])]["tardiness"] + 1
                }
        else:
            res[tuple(liste)]= {
                "finished": res[tuple(liste[:l-1])]["finished"] + P[liste[l-1]],
                "tardiness": res[tuple(liste[:l-1])]["tardiness"]
                }

