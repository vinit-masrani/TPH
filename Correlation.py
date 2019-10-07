x = str(input("Enter the first signal values seperated by space : "))
y = str(input("Enter the second signal values separated by space : "))

def crosscorrelation(x, y):
    x = x.split(' ')
    y = y.split(' ')
    xlist = [int(i) for i in x]
    ylist = [int(i) for i in y]
    print("\nThe First Signal Is : ",xlist,"\nThe Second Signal Is : ",ylist)
    m = len(xlist)
    n = len(ylist)
    for i in range(0,int(n/2)):
        temp = ylist[i]
        ylist[i] = ylist[n-1-i]
        ylist[n-1-i] = temp
    a=[[0 for i in range(n)] for j in range(m)]
    for i in range (0,m):
        for j in range (0,n):
            a[i][j] = xlist[i] * ylist[j]
    totlen = m + n - 1
    ccor = []
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
        ccor.append(subtot)
    return ccor
crosscorrelationlist = crosscorrelation(x,y)
print("Cross Correlation Between Them Is : ",crosscorrelationlist)

def autocorrelation(x):
    x = x.split(' ')
    y = x
    xlist = [int(i) for i in x]
    ylist = [int(i) for i in y]
    print("\nThe First Signal Is : ",xlist,"\nThe Second Signal Is : ",ylist)
    m = len(xlist)
    n = len(ylist)
    for i in range(0,int(n/2)):
        temp = ylist[i]
        ylist[i] = ylist[n-1-i]
        ylist[n-1-i] = temp
    a=[[0 for i in range(n)] for j in range(m)]
    for i in range (0,m):
        for j in range (0,n):
            a[i][j] = xlist[i] * ylist[j]
    totlen = m + n - 1
    ccor = []
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
        ccor.append(subtot)
    return ccor
autocorrelationlist = autocorrelation(x)
print("Auto Correlation Between Them Is : ",autocorrelationlist)
