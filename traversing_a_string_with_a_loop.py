index = 0 
fruit = 'strawberry'
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

    #output:
# s
# t
# r
# a
# w
# b
# e
# r
# r
# y

#Corey Schafer slicing strings and lists video:

#slicing: a way to extract certain parts of a list

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#positive indexes for the above:   0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#negative indexes for the above: -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

print (my_list[0])
#output: 0

print (my_list[-1])
#output: 9

print (my_list[-9])
#output: 1

#How do you extract a certain range from this list?
#use: list[start:end:step]
#end is non-inclusive

print(my_list[0:5])
#output:[0, 1, 2, 3, 4]

#if you wanted to include 5, you need to go to end of 6:
print(my_list[0:6])
#output: [0, 1, 2, 3, 4, 5]

#if you wanted values 3 through 7:
print(my_list[3:8])
#output: [3, 4, 5, 6, 7]

#if I wanted 3 through 7: (using the negative number thing above:)
print(my_list[-7:-2])
#output:[3, 4, 5, 6, 7]

#you can mix and match positive and negative values:
print(my_list[3:-2])
#output:[3, 4, 5, 6, 7]

#also: with the mix and match
print(my_list[-7:8])
#output: [3, 4, 5, 6, 7]

#if you want to print the whole list: don't have a second number after the colon:
print(my_list[1:])
#output:[1, 2, 3, 4, 5, 6, 7, 8, 9]

#beginning with a colon also works:
#-1 is 9, and because the list ending is NON inclusive, it won't include 9

print(my_list[:-1])
#output: [0, 1, 2, 3, 4, 5, 6, 7, 8]

#to print the whole list:
print(my_list[:])
#output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#how to use steps:
#form: list[start:end:step] 
#allows us to skip values:

#start at value 2, go to 8:
print(my_list[2:-1])
#output:[2, 3, 4, 5, 6, 7, 8]

#use a step of two to skip values:
print(my_list[2:-1:2])
#output: [2, 4, 6, 8]

#printing a step of 1 is the same as having no step, it's the default
print(my_list[2:-1:1])
#output:[2, 3, 4, 5, 6, 7, 8]

#can print a negative step:
print(my_list[2:-1:-1])
#output: []
#empty array

#start at -1 to 2 (or from 9 to 2) and go in reverse:
#end index is still non inclusive
print(my_list[-1:2:-1])
#output:[9, 8, 7, 6, 5, 4, 3]

#how would you go from 8 down to 2 inclusive of 2 with a step of 1
print(my_list[-2:-9:-1])
#output: [8, 7, 6, 5, 4, 3, 2]

#if you want the entire thing in reverse:
print(my_list[::-1])
#output:[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#slicing strings

sample_url = 'https://coreyms.com'
print(sample_url)
#output: https://coreyms.com

#reverse the url:
print(sample_url[::-1])
#output:moc.smyeroc//:sptth

#get the top level domain:
print(sample_url[-4:])
#output: .com

#print the url without the https://
print(sample_url[8:])
#output:coreyms.com

#print the url without the https:// or the top level domain:
print(sample_url[8:-4])
#output: coreyms