from operator import itemgetter
from dataExtractor import getData3



def moore(tasks,n):
  tasks = sorted(tasks, key=itemgetter(2))
  T=[]
  V=[]
  somme=0
  for i in range(n):
    x=tasks[i]
    T.append(x)
    if x[1]+somme>x[2]:
      V.append(max(T, key=lambda y: y[1]))
      T.remove(max(T, key=lambda y: y[1]))
    else:
      somme=somme+x[1]
  return V

T = getData3('../instances/P1_n50.txt')

print(len(moore(T,len(T))))




"""
T=[
   [1,24,57],
   [2,1,144 ],
   [3,47,46],
   [4,48,214],
   [5,4,162],
   [6,23,96],
   [7,41,219],
   [8,18,235],
   [9,19,74],
   [10,50,184],
   [11,12,14],
   [12,30,36],
   [13,15,9],
   [14,60,38],
   [15,57,24],
   [16,144,1 ],
   [17,46,48],
   [18,214,214],
   [19,162,50],
   [20,96,96],
]
"""


