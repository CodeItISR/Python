# Checks framework

This framework using annotations, it is for adding
conditions for the function's arguments, as easy
and clean as it can get.
It will raise an error with detail,
if the condition is not vaild

python version from 3.3  
## Install:
Go to the comand prompt(cmd) or the terminal and write  
```
pip install Checks
```
If this is not working, Please check if you got pip or try
to specify the full path to it.    
In windows for example:  
```
C:\Users\user\AppData\Local\Programs\Python\Python36-32\Scripts\pip install Checks
```
Other option is to copy the Checks.py file and sabe it in the site-packages in python
directory
#===================================================

## Example 1:
## check if the argument is a integer
```python
from Checks import check, IsInteger

@check
def print_integer(number : IsInteger):
  print(number)
```
@check - the decorator is for executing
the IsInteger function with the value of number
argument, rasie an error if it isnt an Integer  

#===================================================

## Example 2:
This line of code checks if the first argument is a number bigger than 10  
and the second arg is string else raise an error  
```python
from Checks import check, BiggerThan, IsString

@check
def print_message(number : (BiggerThan, 10), msg : IsString):
  print(msg + ' ' + str(number))
```
Using a function in the annotation that is with more than one
argument, use parentheses in the annotation place - 
the function is first and then the other values
BiggerThan is a function with 2 args BiggerThan(value, compare_to)
so in this example it will execute like this: BiggerThan(number, 10)

#===================================================

## Example 3 - custom annotation functions :
Lets create a function that checks if a number is in some sort of range  
To do that there is one function that you need to import besides the check
decorator to execute the annotation,here is the full program:
```python

from Checks import check, check_annotation_error

def BetweenValues(value ,from_number, to_number):  
    condition = '{} > {} and {} < {}'.format(value, from_number, value, to_number)  
    message = 'The number {} need to be between {}-{}'.format(value, from_number, to_number)  
    check_annotation_error(condition, message)  

@check
def add1(a:(BetweenValues,5,10)):
    return a+1

print(add1(9))
```
We created a function called BetweenValues take 3 values:  
value is the number to check  
from_number and to_number is the range  
Then we created the condition to check  
'{} > {} and {} < {}'.format(value, from_number, value, to_number)  
les say the values are (7,5,10) the condition after format will be:  
7 > 5 and 7 < 10  
Then we created a custom message that will raise if the condition is false, 
the main function that makes it append is check_annotation_error(condition, message)  
this function checks the condition, if its false raise an error with that message  

## This framework makes it easy to code
