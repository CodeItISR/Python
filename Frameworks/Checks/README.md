# Checks framework

This framework using annotations, it is for adding
in an easy way functionality to function,
in spasipc for checking conditions on an argument of
the function and raise an error with detail,
if the condition is not vaild
    
#===================================================

## Example 1:
## check if the argument if a integer

@check
def print_integer(number : IsInteger):
  print(number)

@check - is a decorator is for executing
the IsInteger function with the value of number
rasie an error is its not Integer

#===================================================

## Example 2:
check if first argument is a number
bigger than 10
and second arg is string

@check
def print_message(number : (BiggerThan, 10), msg : IsString):
  print(msg + ' ' + str(number))

Using function in the annotation that is with more than one
argument, use a parenthasis in the annotation place as
that the function is first and then the other values
BiggerThan is a function with 2 args BiggerThan(value, compare_to)
so in this example it will execute like this: BiggerThan(number, 10)

#===================================================

## Example 3 - custom annotation functions :
Lets create a function that check if a number is in some sort of range
To do that there is 1 function you need to import, and the check
decorator to execute the annotation,here is the full program:

from Checks import check, check_annotation_error


def BetweenValues(value ,from_number, to_number):
    condition = '{} > {} and {} < {}'.format(value, from_number, value, to_number)
    message = 'The number {} need to be bitween {}-{}'.format(value, from_number, to_number)
    check_annotation_error(condition, message)

@check
def add1(a:(BetweenValues,5,10)):
    return a+1

print(add1(9))

We created a function called BetweenValues take 3 values:
value is the number to check
from_number and to_number is the range
Then we created the condition to check
'{} > {} and {} < {}'.format(value, from_number, value, to_number)
les say the values are (7,5,10) the condition after format will be:
7 > 5 and 7 < 10
Then we create a custom message that will raise if the condition doesnt work
and those main function that makes it append is check_annotation_error(condition, message)
its check the condition and if its false ,raise an error with that message

## This framework make it clean and easy coding