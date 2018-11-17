a=float(input("input a:"))
b=float(input("input b:"))
c=float(input("input c:"))
d=float(input("input d:"))
def f(x):                            #定义函数f(x)
	return float(a*x**3+b*x**2+c*x+d)	
for i in range(-100,100):            #迭代区间左端点
	l=float(i)                       #一定是float
	r=float(i+1)
	if (abs(f(l))<1e-4):             #浮点数比较大小 绝对值小于0.001 即认为是根了
		print("%.2f"%l)              #输出保留2位小数
		continue                     #依条件 这个区间肯定没根了 换下一个区间
	if (f(l)*f(r)<0):                #如果区间中有一个根
		while (abs(l-r)>1e-4):       #如果没有达到精度
			m=(l+r)/2                #取中
			if abs(f(l)*f(m))<1e-4:  #如果根在左区间
				r=m
			else:                    #根在右区间
				l=m
		print("%.2f"%l)       
