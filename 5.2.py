def getInput():
    l=[]
    print("Please input all the numbers one by one")
    print("Press whitespace to quit:")
    while(True):
        b=input()
        if b==" ":
            break
        else:
            l.append(int(b))
    return l


def binarySearch(l,key):
    L=0
    H=len(l)-1
    while L<=H:
        mid=(H+L)//2
        if key>l[mid]:
            L=mid+1
        elif key<l[mid]:
            H=mid-1 
        else:
            return mid
   


if "___name__==__main__":
    l=getInput()
    key=int(input("Please input the key you want to search:"))
    result=binarySearch(l,key)
    if result==None:#若查找失败
        print("NO FOUND!")
    else:#若查找成功，返回位置索引
        print("The index of the key in the list is:",result+1)      
        



    
