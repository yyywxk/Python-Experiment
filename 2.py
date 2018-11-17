infile=open("C:/Users/仰仰仰望星空/Desktop/love.txt")
con=infile.read()
infile.close()
print(con)
infile2=open("D:/冰点文库/kpdf/英文停用词库.txt")
con2=infile2.read()
infile2.close()

hist = dict()
def repl(s):   
    s=s.replace(':',' ')
    s=s.replace('.',' ')
    s=s.replace('"',' ')
    s=s.replace('?',' ')
    s=s.replace(',',' ')
    return s#除去标点
  
con=repl(con)
print(repl(con)) 
def process_file(file):
  for word in file.split():#将单词一个个地拆开
      word=word.lower()#将单词全部变为小写
      hist[word] = hist.get(word,0) + 1#计算出现的频数
  return hist


hist=process_file(con)
list1=hist.keys()
#print(list1)
print('每个单词的使用次数统计如下:')
#print(hist)
def total_words(hist):
      return sum(hist.values())#计算文章总单词数
def different_words(hist):#计算出现不同单词的总数
      return len(hist)
print('全部单词的数量为（个）:',total_words(hist),)
print('出现不同的单词数量为（个）:',different_words(hist))


def substract(list1,list2):
   res=[]
   for v in list1:
          if v not in list2:
              res.append(v)#去除出现在停用表中的单词
   return res


list2=con2.split()
#print(list2)
res= substract(list1,list2)
#print('Words in the love but not in the words list are:',res)

dict1={}
for item in res:
    dict1[item]=hist[item]#将剩下的单词和频数输入一个字典中
#print(dict1)

def most_common(hist):
      t= []
      for key,value in hist.items():
          t.append((value,key))
      t.sort(reverse = True)#倒排序
      return t

t=most_common(dict1)
print('Ten of the most common words are:')
for value,key in t[:10]:#输出前十个单词及其频数
      print (key,'\t',value)
list1=[]
list2=[]
for item in t[:10]:
  list1.append(item[0])#将列表拆成两个列表，且它们一一对应
  list2.append(item[1])
t1=tuple(list1)#将列表转化成元组
t2=tuple(list2)


import numpy as np
import matplotlib.pyplot as plt#调用matplotlib
def main():
     N=10
     ind = np.arange(N) # 获得 x 轴的坐标序列
     width = 0.4
     fig, ax = plt.subplots()
     rects = []
     frequency=t1


     rects.append(ax.bar(ind + width * 1,frequency,width ,color = 'red'))
     ax.set_xlabel('Words')# 设置坐标轴标题
     ax.set_ylabel('Frequency')
     ax.set_title('Words frequency analysis')#设置图形的名字
     ax.set_xticks(ind +1.5* width)
     ax.set_xticklabels(t2)#设置X轴的各柱形的名字

     def autolabel(rects):# 定义函数，在每一个序列的柱形图上显示数值
           for rect in rects:
                 height = rect.get_height()
                 ax.text(rect.get_x()+rect.get_width()/2.,1.00*height,"%d"%int(height),ha="center",va="bottom") # 显示数值，并设定其显示位置

     autolabel(rects[0])
     plt.show()# 显示图形
     
if"__name__==__main__":
       main()





