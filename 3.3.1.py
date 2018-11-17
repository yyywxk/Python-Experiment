import math

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def transform():
    times=0
    while times < secret_list_len:
        times=times+1
        try:
           num=int(alphabet.index(plain[times-1])+int(value))
           if num>25:
                num=int(num%26)
           if num<-25:
                num=int(-(-num%26))
           output=alphabet[num] 
        except IndexError:
            x=ord(plain[times-1])
            y=x+32
            z=chr(y)
            num=int(alphabet.index(z)+int(value))
            if num>25:
                num=int(num%26)
            if num<-25:
                num=int(-(-num%26))
            output=alphabet[num]
        except ValueError:
            output=plain[times-1]
        print(output,end='')
print("")

plain=input("请输入明文: ")
value=input("设定一个位移值: ")
value=int(value)
secret_list=list(plain)
secret_list_len=len(secret_list)
print("")
print("密文:",end='')
transform()




