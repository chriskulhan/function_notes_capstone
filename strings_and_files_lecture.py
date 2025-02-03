##Python Strings

#str() 
#immutable, cannot be changed once they are written
#access strings using [] brackets
#backslash used to include quotes \'\"

##len works on strings, lists, etc.
##len(string)
#returns the length of the string
s = 'hi'
print(s[1])
#output: i
print (len(s))
#output: 2
print (s + ' there')
#output: hi there

##What is a string?
    #A sequence of characters
    #access the characters with the bracket operator:
fruit = 'banana'
#0 is the index
letter = fruit[0]
print (letter)  
#output: b (the 1st letter of banana
  
#Textual data 
#print('Hello world!')
#output: Hello world!

my_message = "Hello world2!"
print(my_message)
#output:Hello world2!

another_message = "Chris's world"
another_message2 = 'Chris\'s other world'
print(another_message)
#output: Chris's world
print(another_message2)
#output:Chris's other world

#use 3 quotes before and after the message to have contents and print out go on two lines: 
try_three_quotes = """How to print on 
two lines"""
print(try_three_quotes)
#output:
#How to print on 
#two lines

#Access individual characters:
#len 
message_again = 'Hello sun!'
print(len(message_again))
#output: 10

#access characters individually: index starts at zero:
print(message_again[4])
#output:o

#access a range of characters:
print(message_again[0:5])
#includes the zero index, up to but not including 5
#output: Hello

#another way:
print(message_again[:5])
#output: Hello

#if we want to start in the middle of a string and go to the end:
print(message_again[6:])
#output: sun!

#Difference between a method and a function
#method is a function that belongs to an object

#lowercase:
print(message_again.lower())
#output: hello sun!

#uppercase:
print(message_again.upper())
#output: HELLO SUN!




#Use string methods to perform operations on strings
#Open files and read them to load info into applications
#Write files to have info persist

