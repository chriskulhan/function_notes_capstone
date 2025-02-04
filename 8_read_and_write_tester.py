
#have the original file opened (test.txt)
with open ('test.txt', 'r') as rf:
    #have a file that doesn't have anything in it yet (test_copy.txt)
    with open ('test_copy.txt', 'w') as wf:
        #loop read through the lines in the first file test.txt, 
        # and write them into the second file test_copy.txt
        for line in rf:
            wf.write(line)
            #when I run this, it will create an exact copy of the original file. 