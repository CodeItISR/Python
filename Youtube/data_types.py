# KEY : VALUE - to get a value need to access it like a list with the key
# key can be string or int or float, but it need to be uniqe

# Creating an dictionary
dictionary = {1: 2 ,"B": "hello" , "C" : 5.2}

# Adding a Key "D" with value awesome
dictionary["D"] = "awesome"
print(dictionary["D"])
# Print the dictionary as list of tuples
print(list(dictionary.items()))

#====================
# tuple is like a list except its static, cant change the values
# 1 item tuple need to be with comma (50, )

# Create a tuple variable
tup = (1,2,3)

# Print the second item
print(tup[1])

#====================
# multi dimensional list
# contain list that have items that can be list

# set the variable to be a list with list item
list_of_lists = [[1,2,3], ["hello", "1"], 5]

print(list_of_lists[0])    # print the first item - [1,2,3]
print(list_of_lists[1][0]) # print the first item in the second item of the all list - hello
print(list_of_lists[2])    # print the third item - 5
