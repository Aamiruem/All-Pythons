class Rectangle:
    
    def __init__(self, height, width):
        print(f"A rectangle is created with height: {height} and width: {width}")
        self.height = height
        self.width = width
    
    def set_dimension(self, height, width):
        self.height = height
        self.width = width
        
    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2*(self.height + self.width)

# creating object
rectangle1 = Rectangle(4,3)
rectangle1 = Rectangle(5,6)
rectangle1 = Rectangle(8,7)
rectangle1 = Rectangle(9,4)








