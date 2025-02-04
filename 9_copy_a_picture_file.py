#will not work like This: 

# with open ('IMG7178.JPG', 'r') as rf:
#     #have a file that doesn't have anything in it yet (test_copy.txt)
#     with open ('IMG7178_copy.JPG', 'w') as wf:
#         #loop read through the lines in the first file test.txt, 
#         # and write them into the second file test_copy.txt
#         for line in rf:
#             wf.write(line)

#will need to read and write in binary in order to copy the file:
#change r to rb and w to wb

# with open ('IMG_7178.JPG', 'rb') as rf:
#     with open ('IMG_7178_copy.JPG', 'wb') as wf:
#         for line in rf:
#             wf.write(line)
            #made a copy of the photo!!!! (I'm shook!)

#Maybe you want to do this is different chunk sizes:
with open ('IMG_7178.JPG', 'rb') as rf:
    with open ('IMG_7178_copy.JPG', 'wb') as wf:
        #create a chunk size:
        chunk_size = 4096
        #read each chunk size in turn
        rf_chunk = rf.read(chunk_size)
        #create a loop to read until there is nothing left to read in our copy:
        #while the length of the chunk is greater than zero
        while len(rf_chunk) > 0:
            #keep reading
            wf.write(rf_chunk)
            #make sure it's not an infinite loop read in the next chunk size from the original file:
            rf_chunk = rf.read(chunk_size)

            #delete copy to see if it works again

            #It worked again!!! (but it took a little longer.)