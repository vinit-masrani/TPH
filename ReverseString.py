def reverseString(exp,n):
    if length(exp) < 2:return exp
    elif n is 1 : return exp[::-1]
    elif n is 2: return ' '.join(i[::-1] for i in exp.split(' '))
