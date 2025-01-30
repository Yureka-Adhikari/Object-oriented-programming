class student:
    grade = 8
    print("Hi I am in grade ", grade)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
ob1 = student("Yureka", 14)
print(ob1.name)
print(ob1.age)