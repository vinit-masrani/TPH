import matplotlib.pyplot as plt
rmin = int(input("Enter The Rmin For Original Gray Level Of Image : "))
rmax = int(input("Enter The Rmax For Original Gray Level Of Image : "))
ranger = rmax - rmin + 1
Grayr = []
nkr = [0 for r in range(0,ranger)]
j = 0
for i in range(rmin,(rmax+1)):
    Grayr.append(i)
    print("Enter nkr For The Gray Level ",i," : ")
    temp = int(input())
    nkr[j] = temp
    j = j + 1
    
smin = int(input("Enter The Smin For Linearly Streched Gray Level Of Image : "))
smax = int(input("Enter The Rmax For Linearly Streched Gray Level Of Image : "))
ranges = smax - smin + 1
Grays = []
nks = [0 for r in range(0,ranges)]
for i in range(smin,(smax+1)):
    Grays.append(i)
j = 0
for i in range(rmin,(rmax+1)):
    temp = (smax - smin) / (rmax - rmin) * (i - rmin) + (smin)
    temp = round(temp)
    print(temp,i,Grayr[i])
    nks[temp] = nkr[i]
print(nks)
plt.stem(Grayr,nkr)
plt.title("Original Histogram Of Image")
plt.xlabel("Gray Scale Value->")
plt.ylabel("Number Of Pixels->")
plt.show()
plt.stem(Grays,nks)
plt.title("Linearly Scaled Histogram Of Image")
plt.xlabel("Gray Scale Value->")
plt.ylabel("Number Of Pixels->")
plt.show()
