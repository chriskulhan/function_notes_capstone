#What if we try to write within a file that we have open in read mode?

# with open('test.txt', 'r') as f:
#     f.write('Test')
    #output: io.UnsupportedOperation: not writable

#Create a new file and then change the character from an r to a w:
#Be careful, if you use w on a file that already exists, it will overwrite it.

# with open('test2.txt', 'w') as f:
#     f.write('Test')
    #output: made a new file: test2.txt, and wrote Test in it.

# with open('test2.txt', 'a') as f:
#     f.write('Test again') 
    #output: now the test2.txt file is: TestTest again

# with open('test2.txt', 'a') as f:
#     f.write('\nTest again') 
    #output to test2.txt:
# TestTest again
# Test again

#this will create a file but not write anything in it:
# with open('test3.txt', 'w') as f:
#     # pass
    #output: file created but nothing in it.
   
#Use seek to write at the beginning of the file:
with open('test3.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('RR')
    #output: it wrote Test, then seek went to the beginning and overwrote RR from the 0 position
    #SO the output: RRst

    

