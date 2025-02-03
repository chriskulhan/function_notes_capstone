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

#another way, includes everything before the character after the colon:
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

#count the number of something we want to find:
#look for Hello:
print(message_again.count('Hello'))
#output: 1
#because there is one Hello in 'Hello sun'

#count the number of l s in the message_again:
print(message_again.count('l'))
#output: 2

#where is the index of certain argument (or what we want to find)
print(message_again.find('sun'))
#output: 6
#because sun starts at the 6th index

#if use find and it doesn't exist, python will return -1:
print(message_again.find('world'))
#output: -1

#replace characters with other characters:
message_again.replace('sun', 'world')
print(message_again)
#output: Hello sun!
#because we need to replace into a new variable

#make a new variable to allow to replace the characters:
message_again_replace1 = message_again.replace('sun', 'world')
print(message_again_replace1)
#output: Hello world!

#if you really want to replace what's in the original variable, you can reset the variable:
message_again = message_again.replace('sun', 'world')
print(message_again)
#output: Hello world!
#now message_again is Hello world! instead of Hello sun!

#how to add multiple strings an concatenate them together:
greeting = 'Hello'
name = 'Chris'

full_message = greeting + name
print(full_message)
#output: HelloChris

#need to add spaces:
full_message = greeting + ', ' + name
print(full_message)
#output: Hello, Chris

#add to end of message
full_message = greeting + ', ' + name + '. Welcome!'
print(full_message)
#output: Hello, Chris. Welcome!

#formatted string, allow to type as it would appear:
full_message = '{}, {}. Welcome!'.format(greeting, name)
print(full_message)
#output: Hello, Chris. Welcome!

#using f strings:, make string formatting as simple as possible
full_message = '{greeting}, {name}. Welcome!'
print(full_message)
#output: {greeting}, {name}. Welcome! 
#!!!forgot the f

#try again:
full_message = f'{greeting}, {name}. Welcome!'
print(full_message)
#output: Hello, Chris. Welcome!

#using f strings, you can manipulate the variable inside the curly braces:
full_message = f'{greeting.lower()}, {name.upper()}. Welcome!'
print(full_message)
#output:hello, CHRIS. Welcome!

#if you are curious about what attributes and methods that are available with a certain variable:
#use dir(variable)
print(dir(name))
#output:
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
# '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', 
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', 
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', 
# '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 
# 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 
# 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
# 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 
# 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 
# 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

#that ^^doesn't say what any of these do, to see that, use the help function:
# you need to ask python for help on the class of the variable, not the name of the variable:
#print(help(str))

#output SUPER LONG:
#Help on class str in module builtins:

# class str(object)
#  |  str(object='') -> str
#  |  str(bytes_or_buffer[, encoding[, errors]]) -> str
#  |
#  |  Create a new string object from the given object. If encoding or
#  |  errors is specified, then the object must expose a data buffer
#  |  that will be decoded using the given encoding and error handler.
#  |  Otherwise, returns the result of object.__str__() (if defined)
#  |  or repr(object).
#  |  encoding defaults to sys.getdefaultencoding().
#  |  errors defaults to 'strict'.
#  |
#  |  Methods defined here:
#  |
#  |  __add__(self, value, /)
#  |      Return self+value.
# etc.....


#Use string methods to perform operations on strings
#Open files and read them to load info into applications
#Write files to have info ppersist

#find information on a specific function:

print(help(str.lower))

#output:##this didn't work..

#Corey Schafer video: CoreyMS.com