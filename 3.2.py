dictionary={}
def add_dict(dictionary,en,ch):
    dictionary[en]=ch
    dictionary[ch]=en
    print("添加成功")
def find(dictionary,string):
    if string in dictionary:
        print("该单词",string,"的意思是:",dictionary[string])
    else:
        print("该单词不在词典内")    


i=0
while i<10:
   en=input("增添的英语单词:")
   ch=input("对应的中文单词:") 
   add_dict(dictionary,en,ch)
   i=i+1
   
  
string=input("请输入单词:")
find(dictionary,string)
