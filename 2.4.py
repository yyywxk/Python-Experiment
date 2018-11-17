def Factorial(n):
    n=int(n)
    if n<0:
        print("错误信息")
    elif  n==0:
        print("1")
    else:
        m=n-1
        while m>0:
            n=n*m
            m=m-1
    return n

import math
A=Factorial(10)
B=Factorial(8)
C=Factorial(7)
D=Factorial(6)
X=A/B
Y=B/C
Z=C/D
result=X*Y*Z
print("不同的选法有",int(result),"种")
      


         
