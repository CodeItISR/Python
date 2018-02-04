# program 1
#defining a function that get a input from the user print it and return it

def get_name():
    name = input("Enter your name: ")
    print("Hello " + name)
    return name

#defining a function that get a string variable (name) and retrun its lenght. equivalent to len(var)
def lenght(name):
    l = 0
    for i in name:
        l = l + 1
    return l
    
user_name = get_name()             # set name to the user input
name_lenght = lenght(user_name)    # set lenght to the return value of the lenght function
print(name_lenght)

#===================================
#program 2 - wont change the value of the num

def a(num)
  num = num + 1

num = 1
a(num)
print(num)                        # output : 1 

===================================
#program 3 - change the value of the num
# when change a variable in a function, it create a local variable that applies only to the function
                                              #the same
def a(num)                                    def a(num)
  num = num + 1                                 num = num + 1
  return num                                    return num
  
num = 1                                       number = 1
num = a(num)                                  nummber = a(number)
print(num)        # output : 2                print(number)
c = 1

===================================
#program 4 - change the value of the num using global

num = 1

def a():
    global num                              # define that var num is global - uses the outside var
    num = num + 1

a()
print(num)                                 # output : 2 








