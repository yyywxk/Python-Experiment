import tkinter 
from tkinter import * 
from tkinter import messagebox 

def main(): 
    root = Tk()# 创建 GUI 主程序 
    calculator = Label(root)# 创建主窗口 
    calculator.pack(fill=BOTH, expand = 1) 

    addWidgets(calculator)# 调用函数，向窗口上添加功能按钮，以输入数字和运算符 
    root.title('Calculator')
    root.wm_resizable(width = False, height = False) # 禁用窗口缩放 
    root.mainloop() 

def addWidgets(frame): 
    expression = Text(frame, height = 2, width = 28) # 创建表达式输入窗口 
    # 创建数字按钮 
    number_1 = Button(frame, text='1', width = 5, command = lambda: input_char('1', expression))  
    number_2 = Button(frame, text='2', width = 5, command = lambda: input_char('2', expression))
    number_3 = Button(frame, text='3', width = 5, command = lambda: input_char('3', expression))
    number_4 = Button(frame, text='4', width = 5, command = lambda: input_char('4', expression))
    number_5 = Button(frame, text='5', width = 5, command = lambda: input_char('5', expression))
    number_6 = Button(frame, text='6', width = 5, command = lambda: input_char('6', expression))
    number_7 = Button(frame, text='7', width = 5, command = lambda: input_char('7', expression))
    number_8 = Button(frame, text='8', width = 5, command = lambda: input_char('8', expression))
    number_9 = Button(frame, text='9', width = 5, command = lambda: input_char('9', expression))
    number_0 = Button(frame, text='0', width = 5, command = lambda: input_char('0', expression))

    # 创建运算符输入按钮
    btn_add = Button(frame, text = '+', width = 5,  command = lambda: input_char('+', expression)) 
    btn_subtract = Button(frame, text = '-', width = 5,  command = lambda: input_char('-', expression))
    btn_multiply = Button(frame, text = '*', width = 5,  command = lambda: input_char('*', expression)) 
    btn_divide = Button(frame, text = '/', width = 5,  command = lambda: input_char('/', expression)) 
    btn_equal = Button(frame, text = '=', width = 5,  command = lambda: input_char('=', expression)) 
    #btn_point = Button(frame, text='.', width=5, command=lambda: input_char('.', expression))
    
    parenthesis_l=Button(frame, text='(', width=5, command=lambda: input_char('(', expression))
    parenthesis_r=Button(frame, text=')', width=5, command=lambda: input_char(')', expression))
    
    empty=Button(frame, text='clear', width=5, command=lambda:addWidgets(frame))
    
    # 使用 grid_configure 函数将组件添加到主窗口上 
    expression.grid_configure(column = 1, row = 2, columnspan = 4, rowspan = 1)  
    number_1.grid_configure(column = 1, row = 3, columnspan = 1, rowspan = 1) 
    number_2.grid_configure(column = 2, row = 3, columnspan = 1, rowspan = 1)
    number_3.grid_configure(column = 3, row = 3, columnspan = 1, rowspan = 1)
    number_4.grid_configure(column = 1, row = 4, columnspan = 1, rowspan = 1)
    number_5.grid_configure(column = 2, row = 4, columnspan = 1, rowspan = 1)
    number_6.grid_configure(column = 3, row = 4, columnspan = 1, rowspan = 1)
    number_7.grid_configure(column = 1, row = 5, columnspan = 1, rowspan = 1)
    number_8.grid_configure(column = 2, row = 5, columnspan = 1, rowspan = 1)
    number_9.grid_configure(column = 3, row = 5, columnspan = 1, rowspan = 1)
    number_0.grid_configure(column = 1, row = 6, columnspan = 1, rowspan = 1)
    
    btn_add.grid_configure(column = 4, row = 3, columnspan = 1, rowspan = 1)
    btn_subtract.grid_configure(column = 4, row = 4, columnspan = 1, rowspan = 1)
    btn_multiply.grid_configure(column = 4, row = 5, columnspan = 1, rowspan = 1)
    btn_divide.grid_configure(column = 4, row = 6, columnspan = 1, rowspan = 1)
    btn_equal.grid_configure(column = 3, row = 7, columnspan = 1, rowspan = 1)
    #btn_point.grid_configure(column = 2, row = 6, columnspan = 1, rowspan = 1)
    
    parenthesis_l.grid_configure(column = 2, row = 6, columnspan = 1, rowspan = 1)
    parenthesis_r.grid_configure(column = 3, row = 6, columnspan = 1, rowspan = 1)
    
    empty.grid_configure(column = 1, row = 7, columnspan = 1, rowspan = 1)
    
def input_char(char, expressionview):  
    if char == "=":
        expressionview.insert('1.end', calcu(expressionview))
    else:
        expressionview.insert('1.end', char) # 输入按钮对应的字符 
   
def calcu(expressionview): 
    ''' 
    计算表达式的值，返回结果的字符串形式。 
    如果表达式不合法，返回错误信息 
    ''' 
    equal_str = expressionview.get('1.0', '1.end') 
    expressionview.insert('1.end', '=') 

    s = [] 
    i = 0 
    equal_list = [] #存放后缀表达式
    while i < equal_str.__len__(): 
        if equal_str[i] <= '9' and equal_str[i] >= '0': 
            tmp = 0 
            while i < equal_str.__len__() and equal_str[i] <= '9' and equal_str[i] >= '0': 
                tmp = tmp * 10 + (ord(equal_str[i]) - ord('0')) 
                i = i + 1 
            equal_list.append(tmp) 
            continue 
        else: 
            if equal_str[i] == '(': 
                s.append(equal_str[i]) 
            elif equal_str[i] == ')': 
                try: 
                    while s[s.__len__()-1] != '(': 
                        equal_list.append(s.pop()) 
                    s.pop()   
                except IndexError: 
                    return 'Invalid expersion!' 
            elif equal_str[i] == '+' or equal_str[i] == '-': 
                while s.__len__() > 0 and s[s.__len__()-1] != '(': 
                    equal_list.append(s.pop()) 
                s.append(equal_str[i]) 
            elif equal_str[i] == '*' or equal_str[i] == '/': 
                while s.__len__() > 0 and (s[s.__len__()-1] == '*' or s[s.__len__() - 1] == '/'): 
                    equal_list.append(s.pop()) 
                s.append(equal_str[i]) 
            i += 1 

    while s.__len__() > 0: 
        equal_list.append(s.pop()) 

    # print(equal_list) # print the postfix expression 

    cnt_num = 0 
    cnt_op = 0 
    for item in equal_list: 
        if type(item) == type(0): # integer. 
            cnt_num += 1 
        else: 
            cnt_op += 1 
    if cnt_op != cnt_num - 1: 
        return 'Invalid expersion!' 
     
    ans = [] #利用后缀表达式求结果
    for i in range(0, equal_list.__len__()): 
        if equal_list[i] == '+': 
            ans.append(ans.pop(ans.__len__()-2) + ans.pop(ans.__len__()-1))           
        elif equal_list[i] == '-': 
            ans.append(ans.pop(ans.__len__()-2) - ans.pop(ans.__len__()-1))     
        elif equal_list[i] == '*': 
            ans.append(ans.pop(ans.__len__()-2) * ans.pop(ans.__len__()-1))  
        elif equal_list[i] == '/': 
            try:
                ans.append(ans.pop(ans.__len__()-2) / ans.pop(ans.__len__()-1))  
            except ZeroDivisionError: 
                return 'ZeroDivisionError: division by zero' 
        else: 
            ans.append(equal_list[i]) 

    return str(ans[0]) #返回表达式的最终结果

if __name__ == '__main__': 
    main()
