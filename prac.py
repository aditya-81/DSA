n = 4
x = [-1]*(n+1)
print(x)
def place(k,j):
    for i in range(1,k):
        if ((x[i]==j) or (abs(x[i]-j) == abs(i-k))):
            return False
    return True

def nqueen(k,n):
    global x
    for j in range(1,n+1):
        if place(k,j):
            x[k]=j
            if(k==n):
                print(x[1:])
            else:
                nqueen(k+1,n)




