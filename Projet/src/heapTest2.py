file = open("./result500.txt", "w")

def heapPermutation(a,size):
    global file
    if size == 1:
        file.write(str(a)+",")
        return
    for i in range(size):
        heapPermutation(a, size-1)
        
        if size & 1:
            a[0], a[size-1] = a[size-1], a[0]
        else:
            a[i], a[size-1] = a[size-1], a[i]

a = [
1,
2,
3,
4,
5,
6,
]



n = len(a)
heapPermutation(a, n)

file.close()