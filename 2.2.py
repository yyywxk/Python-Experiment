def Conjecture(n):
    c=0
    while(n!=1):
        c=c+1
        if n%2==0:
            n=int(n/2)
            print("此时N为偶数，第"+str(c)+"次变换的结果是: "+str(n))
        else:
            n=int(n*3+1)
            print("此时N为奇数，第"+str(c)+"次变换的结果是: "+str(n))
    print("该数共经过"+str(c)+"次变换，得到自然数1")
    return
        
n=int(input("请输入任意一个自然数N:"))
print("其角谷猜想的变换过程如下:")
k=Conjecture(n)


                
