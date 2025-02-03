#read method reads a string from an open file
#Syntax: fileObject.read([count])

#example code
#!/usr/bin/python
#open a file
fo = open("food.txt", 'r+')
#9 is the number of bits that will be read:
str = fo.read(9)
print("Read string is : ", str)
#output: Read string is :  Pizza is 