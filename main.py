# Class creation
class myClass:
    
    # Private variable
    __privateVar = 27;
    
    # Private method
    def __privateMeth(self):
        print("I'm inside class myClass")
        
        # Function to print value inside of private variable
        def hello(self):
            print("Private variable value is: ", myClass.__privateVar)
            
# Object creation and Method call
foo = myClass()
foo.hello()
foo.__privMeth

class Computer:
    def __init__(self):
        self._maxprice = 900
    
    def sell(self):
        print('Selling Price: {}'.format(self._maxprice))
    
    def setMaxPrice(self, price):
        self._maxprice = price
        
c = Computer()
c.sell()

# Change the price
c.__maxprice = 1000
c.sell()

# Using Setter Function
c.setMaxPrice(1000)
c.sell()

# Create Class
class Point: 
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        
    # Method to print points in coordinates format
    def __str__(self):
        return "({0},{1})".format(self.__x, self.__y)

# Create Object
p1 = Point(2, 3)
print(p1)  
