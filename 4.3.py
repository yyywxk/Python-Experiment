class Queue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

if"__name__==__main__":
   def hotpotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)      #construct queue

    print(simqueue.items)   
    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
            print(simqueue.items)
        simqueue.dequeue()

    return simqueue.dequeue()


namelist={}
def add_namelist(namelist,a):
    namelist[a]=a
num=input("请输入一个常数:")
num=int(num)
S=input("请输入人数:")
S=int(S)
i=0
while i<S:
    a=input("请输入名字:")
    add_namelist(namelist,a)
    i=i+1
    

print("the lsat one is",hotpotato(namelist,num)) 
