class Circle:
    def __init__(self,pi,d,r):
        self.pi =pi
        self.d =d
        self.r =r
    
    def getArea(self):
       a=pow(self.r,2)
       sol= self.pi * a
       return sol
     
    def getCircumference(self):
       result= 2 * self.pi* self.d
       return result
   
circle1 = Circle(3.14 ,8,2)
print(circle1.getArea())
print(circle1.getCircumference())
    
        
