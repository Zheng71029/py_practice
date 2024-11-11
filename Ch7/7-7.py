class Employee():
    #(a)
    payRate=[1,1.2,1.5]
    def __init__(self,base):
        self.baseSalary=base
    def salary(self,hr,bonus):
        return round(self.baseSalary*hr*self.payRate[bonus])
    #(b)
    @classmethod    
    def set_payRate(cls,new_payRate):
        cls.payRate=new_payRate
    #(c)
    @staticmethod
    def estimate(bs,hr,rate):
        return round(bs * hr * rate)
    
#7-1
tom=Employee(160)
tom.salary(10,1)

#7-2
tom.set_payRate([1,1.3,1.5])

Employee.payRate
print(tom.salary(10,1))

#7-3
print(Employee.estimate(160,10,1.25))