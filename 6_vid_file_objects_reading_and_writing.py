#File objects

#get a file object. 
#created a test.txt file

#bad way to open a file for reading, if no second article opens for reading:
# f = open('test.txt')

# f = open('test.txt', 'r')

# #for writing: 'w'
# #for appending 'a'
# #for reading and writing 'r+'

# print(f.name)
# #output:test.txt

# #to figure out which mode you are using:
# print(f.mode)
# #output: r

# #when you open a file, you must close it:
# f.close()

#Context manager opening a file instead is best practice
#this will automatically close everything
#does the same as above^^
#f is available after the file is closed, but we can't read from it.
# with open('test.txt', 'r') as f:
    # pass

# print(f.mode)
# #output: r

#can't read the file outside of the with block.
# print(f.read())
#output:ValueError: I/O operation on closed file.

#open a file with a context manager:
# with open('test.txt', 'r') as f:
#create a variable to hold contents of file:
    # f_contents = f.read()
    # print(f_contents)
# #output:1) This is a test file
# 2) to see if I can open etc.
# 3) third line
# 4) fourth line
# 5) fifth line
# 6) sixth line
# 7) seventh line
# 8) eighth line
# 9) ninth line
# 10) tenth line

#what if you have a large file you don't want to see everything: 
# with open('test.txt', 'r') as f:
    # f_contents_read_lines = f.readlines()
    # print(f_contents_read_lines)
    #output: ['1) This is a test file\n', '2) to see if I can open etc.\n', '3) third line\n', 
    # '4) fourth line\n', '5) fifth line\n', '6) sixth line\n', '7) seventh line\n', 
    # '8) eighth line\n', '9) ninth line\n', '10) tenth line']

    # #Will read the first line of the file, 
    # f_contents_read_line = f.readline()
    # print(f_contents_read_line)
    # #output:1) This is a test file

    # #if you run it again, it will read the next line:
    # f_contents_read_line = f.readline()
    # print(f_contents_read_line)
    # #output: 2) to see if I can open etc.

#to get rid of extra new line add in an empty string in the print statement, that will get rid of the line:
# with open('test.txt', 'r') as f:
     #Will read the first line of the file, 
    # f_contents_read_line = f.readline()
    # print(f_contents_read_line, end = '')
   
    # #if you run it again, it will read the next line:
    # f_contents_read_line = f.readline()
    # print(f_contents_read_line, end = '')
    #output: 
    #1) This is a test file
    #2) to see if I can open etc.

#How can we read all of the content in a large file? (Use a loop to print each line)
# with open('test.txt', 'r') as f:
    # for line in f:
    #     print(line, end = '')
        #output:
        # 1) This is a test file
        # 2) to see if I can open etc.
        # 3) third line
        # 4) fourth line
        # 5) fifth line
        # 6) sixth line
        # 7) seventh line
        # 8) eighth line
        # 9) ninth line
        # 10) tenth line

#To get more control about what we read:     
# with open('test.txt', 'r') as f:
#     f_contents = f.read()
#     print(f_contents, end='')    
    #output:1) This is a test file
            # 2) to see if I can open etc.
            # 3) third line
            # 4) fourth line
            # 5) fifth line
            # 6) sixth line
            # 7) seventh line
            # 8) eighth line
            # 9) ninth line
            # 10) tenth line
#Can specify the amount of data we want to read at a time by passing in the size as an argument (added 100):
# with open('test.txt', 'r') as f:
#     f_contents = f.read(100)
#     print(f_contents, end='')   
#     #output:
#     # 1) This is a test file
#     # 2) to see if I can open etc.
#     # 3) third line
#     # 4) fourth line
#     # 5) fifth line
#     # 6) si          
# #copy f_contents in the same with statement, and the rest of the file will be read in:
#     f_contents = f.read(100)
#     print(f_contents, end='') 
    #So now with both statements, the whole file is read in:
    #output:
    # 1) This is a test file
    # 2) to see if I can open etc.
    # 3) third line
    # 4) fourth line
    # 5) fifth line
    # 6) sixth line
    # 7) seventh line
    # 8) eighth line
    # 9) ninth line
    # 10) tenth line

#How to use a loop that iterates over the file to read parts of the file in chunks at a time:
# with open('test.txt', 'r') as f:

#     size_to_read = 10

#     f_contents = f.read(size_to_read)

    # while len(f_contents) > 0:
    #     #added an asterix so I can see where the loop ends:
    #     print(f_contents, end='*')
    #     #this vv will stop this while loop when there are no more characters left in the file:
    #     f_contents = f.read(size_to_read)
        #output:  1) This is* a test fi*le
                # 2) to s*ee if I ca*n open etc*.
                # 3) third* line
                # 4) f*ourth line*
                # 5) fifth *line
                # 6) si*xth line
                # 7*) seventh *line
                # 8) ei*ghth line
                # *9) ninth l*ine
                # 10) te*nth line*

#show where in the file you are by using f.tell:
# with open('test.txt', 'r') as f:

#     size_to_read = 10

#     f_contents = f.read(size_to_read)    
    
#     print(f.tell())
    #this will be how many characters have been read in so far:
          #output: 10           

#show 
# with open('test.txt', 'r') as f:

#     size_to_read = 10

#     #reads in the the first 10 characters
#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')

#     #stops where that^ left off an reads in the next 10 characters
#     f_contents = f.read(size_to_read)
#     print(f_contents)  

    #output: 
    # 1) This is a test fi

#What if I want the second read to start back at the beginning of the file? (add f.seek)

with open('test.txt', 'r') as f:

    size_to_read = 10

    #reads in the the first 10 characters
    f_contents = f.read(size_to_read)
    print(f_contents, end='')
    #output:1) This is a test fi

    #add f.seek here, this will set the position back at the beginning of the file
    f.seek(0)

    #stops where that^ left off an reads in the next 10 characters
    f_contents = f.read(size_to_read)
    print(f_contents) 
    #output: 1) This is1) This is