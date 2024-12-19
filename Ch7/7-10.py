# 定義 Person 類別
class Person:
    def __init__(self, na):  # 初始化函數
        self.name = na

    def print_name(self):  # 印出 name 的函數
        print(f'name = {self.name}')


# 定義 Student 類別，繼承自 Person
class Student(Person):
    def __init__(self, na, gender):  # 初始化函數，設置 name 和 gender
        super().__init__(na)  # 呼叫父類別的初始化函數設置 name
        self.gender = gender

    def print_info(self):  # 印出 name 和 gender 的函數
        print(f'name = {self.name}, gender = {self.gender}')


# 測試程式
s0 = Student('Mary', 'F')
s0.print_name()  # 應印出 name = Mary
s0.print_info()  # 應印出 name = Mary, gender = F
