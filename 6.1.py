A=[]
def change(A):
    for i in range(0,11,1):
        haschange=False
        for j in range(0,11-i,1):
            if A[j]>A[j+1]:
                temp=A[j]
                A[j]=A[j+1]
                A[j+1]=temp
                haschange=True
                if haschange==False:break
   


A=[2,5,12,20,26,30,31,30,26,19,10,3]
B=[-9,-6,0,8,14,19,22,21,15,8,0,-6]
C=[3,6,9,22,36,74,179,177,53,23,8,2]
change(A)
print("一年内北京市日均最高气温顺序为:",A)
change(B)
print("一年内北京市日均最低气温顺序为:",B)
change(C)

print("一年内北京市平均降水量顺序为:",C)
