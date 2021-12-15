
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


"""
data10=getData("./instances/P1_n10.txt")
data50=getData("./instances/P1_n50.txt")
data200=getData("./instances/P1_n200.txt")
data500=getData("./instances/P1_n500.txt")
"""
