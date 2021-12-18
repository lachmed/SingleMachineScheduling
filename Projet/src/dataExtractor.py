
def getData(path):
    data = {}

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
        data[i]=(int(line2[i-1]),int(line3[i-1]))


    return data 


def getData2(path):
    data = {}

    filee = open(path,"r")

    line1=filee.readline()
    line2=filee.readline()
    line3=filee.readline()
    line4=filee.readline()
    line5=filee.readline()

    filee.close()
        
    line1=line1.replace("\t", " ")
    n=int(line1.split(" ")[0])


    line2=line2.replace("\t", " ")
    line2=line2.replace("\n", " ")
    line2=line2.split(" ")


    line3=line3.replace("\t", " ")
    line3=line3.replace("\n", " ")
    line3=line3.split(" ")
    
    line4=line4.replace("\t", " ")
    line4=line4.replace("\n", " ")
    line4=line4.split(" ")

    line5=line5.replace("\t", " ")
    line5=line5.replace("\n", " ")
    line5=line5.split(" ")

    for i in range(1,n+1):
        data[i]=(int(line2[i-1]),int(line3[i-1]),int(line4[i-1]),int(line5[i-1]))


    return data 

def getData3(path):
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





"""
data10=getData("../instances/P1_n10.txt")
data50=getData("../instances/P1_n50.txt")
data200=getData("../instances/P1_n200.txt")
data500=getData("../instances/P1_n500.txt")
"""

#data10=getData2("../instances/P2_n10.txt")



