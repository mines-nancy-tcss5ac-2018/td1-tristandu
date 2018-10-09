def solve16(n):
    S=0
    k=1
    while (10**k)<=n:
        k+=1
    k-=1
    while k!=-1:
        a=int(n/(10**k))
        S+=a
        n-=a*(10**k)
        k-=1
    return(S)

assert solve16(2**15)==26
print(solve16(2**1000))