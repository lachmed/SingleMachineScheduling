from operator import itemgetter


def getData(path):
    data = []

    filee = open(path,"r")

    line1=filee.readline()
    line2=filee.readline()
    line3=filee.readline()

    filee.close()
        
    line1=line1.replace("\t", " ")
    n=int(line1.split(" ")[0])


    line2=line2.replace("\t", " ")
    line2=line2.replace("\n", " ")
    line2=line2.split(" ")


    line3=line3.replace("\t", " ")
    line3=line3.replace("\n", " ")
    line3=line3.split(" ")


    for i in range(1,n+1):
        tmp=[]
        tmp.append(i)
        tmp.append(int(line2[i-1]))
        tmp.append(int(line3[i-1]))
        data.append(tmp)


    return data 



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
T = getData('../instances/P1_n50.txt')

print("NbRetard",len(moore(T,len(T))))

