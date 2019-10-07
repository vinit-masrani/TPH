import math
seq = str(input("Enter The Values Of Signal For x(n) Separated By Space : "))
def tweedleDFT(n,k):
    a = -2*math.pi*n*k/N
    temp = complex(round(math.cos(a)),round(math.sin(a)))
    return temp

def DFT(seq):
    seq = seq.split(' ')
    seq = [int(i) for i in seq]
    print("Originally Entered x(n) Sequence Is : ",seq)
    N = len(seq)
    mat = [[0 for i in range(0,N)] for j in range(0,N)]
    for i in range(0,N):
        for j in range(0,N):
            mat[i][j] = tweedleDFT(i,j)
    tempxk = [0 for i in range(0,N)]
    for i in range(0,N):
        tempxk[i] = 0
        for j in range(0,N):
            tempxk[i] = tempxk[i] + (mat[i][j] * seq[j])
    return tempxk
 
Xk = DFT(seq)
print("X(k) Sequence Calculated Using DFT Is : ",Xk)
