# the PyT_import.py file , you need it as a seprate file

def multiple_by(number, multi_number):
    return (number * multi_number)

if __name__ == '__main__':
    print('Hello')

#==================================

import time
from PyT_import import multiple_by as mb

def count_ten():
    count = 0
    while(count < 10):
        print(count)
        time.sleep(1)
        count = count + 1
    print(count)

count_ten()

number = 3
number = mb(number, 3)
print(number)
