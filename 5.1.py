for i in range(100,10000001):
    k=str(i)
    n=len(k)
    s=0
    for j in range(1,n+1):
        s=s+int(k[j-1])**n
    if i==s:
        print(i)

    
