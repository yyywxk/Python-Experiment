a=float(input("请输入a:"))
b=float(input("请输入b:"))
c=float(input("请输入c:"))
d=float(input("请输入d:"))
def f(i):
   f=a*i*i*i+b*i*i+c*i+d
   return f

for i in range(-100,101,1):
    if abs(f(i))<1e-4:
       print("结果是:%.2f"%i)
    elif f(i)*f(i+1)<0:
         low=i
         high=i+1
         while abs(f(high)-f(low))>=1e-4:
            mid=(low+high)/2
            if f(low)*f(mid)<0:
                high=mid
            elif f(low)*f(mid)==0:
               print("结果是:%.2f"%mid)
            else:
               low=mid
         print("结果是:%.2f"%mid)     
      
