import math
class Circle:
    def __init__(self,radius):
        self.r=radius
             
    def girth(self):
        g=2*math.pi*int(r)
        return g
    
    def area(self):
        a=math.pi*int(r)*int(r)
        return a
    
    def cylinderArea(self,h):
        A=2*math.pi*int(r)*int(h)+2*math.pi*int(r)*int(r)
        return A
    
    def cylinderVolume(self,h):
        V=math.pi*int(r)*int(r)*int(h) 
        return V
    

if"__name__==__main__":
    r=input("请输入半径:")
    print("圆的半径:",r)
    print("圆周长:",Circle.girth(r))
    print("圆面积:",Circle.area(r)) 
    h=input("请输入圆柱的高:")
    print("圆柱表面积:",Circle.cylinderArea(r,h))
    print("圆柱体积:",Circle.cylinderVolume(r,h))
    print("测试结束")
    
   
