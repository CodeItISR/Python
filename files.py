# r - read , w - write , a -append
# r+ w+ a+ - read and write
# rb wb ab- binary object

#=====================
# open the file with the option to write
# if the file doesnt exist create a new one
# if it exist clean the file from all its content

f = open('contacts.txt', 'w')

f.write('RONA A:0521111111\n') # \n as a new line
f.write('RONA B:0521111112\n')

f.close()

#=====================
# open the file with the option to read

f = open('contacts.txt', 'w')

# print the text as it is
# text = f.read()
# print(text)

lines = f.readlines()   # f.readliens return a list with all the lines
for line in lines:
    print(line)

f.close()

#=====================
# open the file with the option to append

f = open('contacts.txt', 'w')

f.write('RONA C:0521111113\n') #add this line to the end of the file

f.close()
