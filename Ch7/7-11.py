class Triangle:
    def __init__(self,base,height):
        self.__base=base
        self.__height=height
    def area(self):
        return 0.5*self.__base*self.__height
    
t0=Triangle(10,5)
print(t0.area())

t0.__base=40   # 這裡的 __base 是公有的變數，和 self.__base 是不一樣的變數了
print(t0.area())

# new version,add setter
class Triangle:
    def __init__(self,base,height):
        self.__base=base
        self.__height=height
    def area(self):
        return 0.5*self.__base*self.__height
    def set_base(self,ba):   # set private attribute __base
        self.__base=ba
    def set_height(self,hi): # set private attribute __height
        self.__height=hi

t0=Triangle(10,5)
print(t0.area())
t0.set_base(40)
print(t0.area())