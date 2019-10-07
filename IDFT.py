xn = input("Enter The Input Time Signal : ")
xn = xn.split(' ')
xn = [int(n) for n in xn]
print(xn)

def compFFT(l1,l2,w):
    if w == 'w0':
        w = 1
    else:
        w = -1j
    c0 = l1 + w * l2
    c1 = l1 - w * l2
    return (c0 , c1)
    
def FFT(lt):
    s0, s1 = compFFT(lt[0],lt[2],'w0')
    s2, s3 = compFFT(lt[1],lt[3],'w0')
    Xk0, Xk2 = compFFT(s0,s2,'w0')
    Xk1, Xk3 = compFFT(s1,s3,'w1')
    Xk = [Xk0,Xk1,Xk2,Xk3]
    return Xk
    
FFTseq = FFT(xn)
print(FFTseq)
