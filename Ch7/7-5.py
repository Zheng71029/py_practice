class Sphere():
    def __init__(self,r=1):
        self.rad=r
    def __repr__(self):
        return f'Sphere object, rad={self.rad}'
    def volume(self):
        return 4/3 * 3.14 * (self.rad**3)
    def surface_area(self):
        return 4 * 3.14 * (self.rad**2)
    def __str__(self):
        return f'Sphere object, rad={self.rad}, volume={self.volume():.2f}, surface_area={self.surface_area()}'
    
s1=Sphere(5)
s1

s1.volume()

s1.surface_area()

print(s1)