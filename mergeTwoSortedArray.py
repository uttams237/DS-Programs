from sys import stdin


def merge(arr1, n, arr2, m) :
    i,j=0,0
    arr=[]
    while i<n and j<m :
        # arr.append(big (arr1[i] , arr2[j]) )
        if arr1[i]<arr2[j] :
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1

    for k in range(i,n):
        arr.append(arr1[k])
    for k in range(j,m):
        arr.append(arr2[k])

    return arr



#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
        
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()

    ans = merge(arr1, n, arr2, m)
    printList(ans, (n + m))

    t -= 1
