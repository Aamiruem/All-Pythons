# methods overloading
class Add:
    
    def sum(self, a, b):
        print(a + b)
        
    def sum(self, a, b, c):
        print(a + b + c)
        
        
        
# operator overloading 
class ComplexNumber:
    
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def __add__(self, other):
        return ComplexNumber(self.real+other.real, self.img+other.img)
    
c1 = ComplexNumber(1,2)
c2 = ComplexNumber(3,4)

c3 = c1 + c2
print(c3.real, "+ i", c3.img)

    