n=input("折叠次数:")
n=int(n)
m=1/200
for i in range(1,n+1,1):
    m=m*2
m=m/100
print("厚度为",m,"米")
