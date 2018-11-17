#动态规划法解0-1背包问题
def zeroOneknapsack(w,p,m,x):
    #初始化总价值
    #初始化Load[i][j]前i个物品中装入承重量j的背包的物品总价值
    v=0
    n=len(w)-1
    Load=[[0 for col in range(m+1)] for raw in range(n+1)]
    
    #计算Load[i][j]
    for i in range(1,n+1):
        for j in range(1,m+1):
            Load[i][j]=Load[i-1][j]            
            if(j>=w[i])and (Load[i-1][j-w[i]]+p[i]>Load[i-1][j]):
                Load[i][j]=Load[i-1][j-w[i]]+p[i]
    #递推装入背包的物品
    j=m
    for i in range(n,0,-1):
        if Load[i][j]>Load[i-1][j]:
            x[i]="装"
            j=j-w[i]
    #返回最大价值
    v=Load[n][m]
    return v
m=10
w=[0,2,2,6,5,4]
p=[0,6,3,5,4,6]
#计算n的个数
n=len(w)-1
#初始化x列表，该列表表示每个物品是否装入背包的状态，初始状态的时候均为“未装
x=["未装" for raw in range(n+1)]
#调用函数解背包问题
totalV=zeroOneknapsack(w,p,m,x)
print("装入背包中物品的总价值：",totalV)#输出结果
print("物品是否装入背包的状态：",x[1:])

