# VarName.append(Value) adds Value to the end of the list
# programming_languages.append('c++'), result ['python','c','php','asm','c++']
# VarName.insert(Index,Value) adds Value to index place and push the list to right
# programming_languages.insert(1,'c++'), result ['python','c++','c','php','asm']
# VarName.pop(Index) remove the Value in index place and return it(can be saved in variable)
# programming_languages.pop(1), result ['python','php','asm']

# programming_languages[Index] return the value in the index palce , programming_languages[1] is c

program_name = input('Enter a programming language : ')
programming_languages = ['python','c','php','asm']

#x in y check if the value x is in list y
if(program_name in programming_languages):
    print('Great language')
else:
    print('This is our list ',programming_languages)
