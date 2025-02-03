#write method writes any string to an open file
#syntax: fileObject.wring(string)

#example: 
#fo = file object

#this file will be automatically created: 
fo = open ('food.txt', "w")
fo.write( "Pizza is a great food. \n Yeah it's great!! \n")
#close opened file
fo.close()

#run that^^^ and now look at the file foo.txt again. It's been overwritten!

