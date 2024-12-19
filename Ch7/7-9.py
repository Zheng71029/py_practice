class Car:
    def __init__(self,color):
        self.color=color
    def show(self):
        print(f'color={self.color}')

#(a)
class Truck(Car):
    def __init__(self,dr,ow,co):   #(1)
        self.doors=dr
        self.owner=ow
        super().__init__(co)
    def show(self):                #(2)
        print(f'doors={self.doors}, owner={self.owner}, color={self.color}')

Car('red').show()
Truck(2,'Tom','blue').show()