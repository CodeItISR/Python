class Student:

    def __init__(self ,name ,age ,id):
        self.name = name
        self.age = age
        self.id = id

    def birthday(self):
        self.age = self.age + 1
        print("Happy birthday")

    def print_info(self):
        print("name : " + self.name)
        print("age : " + str(self.age))
        print("ID : " + self.id)

# can create many classes as you want, at diffrent variable
s = Student("Ronaldo" ,25 ,"123456789")

print(s.age)
s.birthday()
print(s.age)

print("The info is :")
s.print_info()
