x = str(input("Enter the first signal values seperated by space : "))
y = str(input("Enter the second signal values separated by space : "))

def linearconvolution(x, y):
    x = x.split(' ')
    y = y.split(' ')
    xlist = [int(i) for i in x]
    ylist = [int(i) for i in y]
    print("\nThe First Signal Is : ",xlist,"\nThe Second Signal Is : ",ylist)
    m = len(xlist)
    n = len(ylist)
    a=[[0 for i in range(n)] for j in range(m)]
    for i in range (0,m):
        for j in range (0,n):
            a[i][j] = xlist[i] * ylist[j]
    totlen = m + n - 1
    lconv = []
    jlist = [0 for i in range(m)]
    for i in range(0,totlen):
        subtot = 0
        k = 0
        for j in range(0,m):
            if jlist[j] < n:
                subtot = subtot + a[j][jlist[j]]
                jlist[j] = jlist[j] + 1
                k = k + 1
            if k == i + 1:
                break
        lconv.append(subtot)
    return lconv
linearconvolutionlist = linearconvolution(x,y)
print("Final Convoluted List Is : ",linearconvolutionlist)

def circularconvolution(x, y):
    x = x.split(' ')
    y = y.split(' ')
    xlist = [int(i) for i in x]
    ylist = [int(i) for i in y]
    print("\nThe First Signal Is : ",xlist,"\nThe Second Signal Is : ",ylist)
    m = len(xlist)
    n = len(ylist)
    totlen = max(m,n)
    if m < totlen:
        for i in range(m,totlen):
            xlist.append(0)
    if n < totlen:
        for i in range(n,totlen):
            ylist.append(0)
    a = [[0 for i in range(0,totlen)] for j in range(0,totlen)]
    xtemplist = xlist
    j = 0
    for i in range(0,totlen):
        for k in range(0,totlen):
            a[k][i] = xtemplist[j]
            j = j + 1
            if j == totlen:
                j = 0
        temp = xtemplist[totlen-1]
        xtemplist = [xtemplist[i-1] for i in range(0,totlen)]
        xtemplist[0] = temp
    finalmat = [[0] for i in range(0,totlen)]
    for i in range (0,totlen):
        for j in range(0,totlen):
            finalmat[i][0] = finalmat[i][0] + (a[i][j] * ylist[j])
    finalmat = [finalmat[i][0] for i in range(0,totlen)]
    return finalmat
circularconvolutionlist = circularconvolution(x, y)
print("Final Convoluted List Is : ",circularconvolutionlist)

def linearviacircularconvolution(x, y):
    x = x.split(' ')
    y = y.split(' ')
    xlist = [int(i) for i in x]
    ylist = [int(i) for i in y]
    print("\nThe First Signal Is : ",xlist,"\nThe Second Signal Is : ",ylist)
    m = len(xlist)
    n = len(ylist)
    totlen = m + n - 1
    if m < totlen:
        for i in range(m,totlen):
            xlist.append(0)
    if n < totlen:
        for i in range(n,totlen):
            ylist.append(0)
    a = [[0 for i in range(0,totlen)] for j in range(0,totlen)]
    xtemplist = xlist
    j = 0
    for i in range(0,totlen):
        for k in range(0,totlen):
            a[k][i] = xtemplist[j]
            j = j + 1
            if j == totlen:
                j = 0
        temp = xtemplist[totlen-1]
        xtemplist = [xtemplist[i-1] for i in range(0,totlen)]
        xtemplist[0] = temp
    finalmat = [[0] for i in range(0,totlen)]
    for i in range (0,totlen):
        for j in range(0,totlen):
            finalmat[i][0] = finalmat[i][0] + (a[i][j] * ylist[j])
    finalmat = [finalmat[i][0] for i in range(0,totlen)]
    return finalmat
linearviacircularconvolutionlist = linearviacircularconvolution(x, y)
print("Final Convoluted List Is : ",linearviacircularconvolutionlist)
