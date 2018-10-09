def miroir(n):
    S=0
    L=list(str(n))
    while L!=[]:
        S+=(10**(len(L)-1))*int(L.pop())
    return(S)
        


def isLychrel(n):
    for i in range(50):
       if miroir(n)==n:
           return False
       else:
           n+=miroir(n)
    return True

def solve55():
    S=0
    for n in range(1,10001):
        if isLychrel(n)==True:
            S+=1
    return(S)

assert isLychrel(10677)==True
print(solve55())