#string immutability means you cannot change a single str_1[i] position because when a string is created it is constant, we have to create a whole new string and assign it to our str_1
str_1 = "break_into_pieces"
str_1 = str_1 + "_k"

#string indexes are locations in memory in which each element within the string is stored, it breaks the string into an array or list and you can call an element using str_name[i]
#printing a string calls entire index, prints from 0 -> len(string)

print(str_1[3])
#This prints all indexes
print(str_1)

#To print a RANGE [start:finish]
#print list elements 1,2,3
print(str_1[1:3])

#stepover is at what increment we interact with the memory locations, [1:5:2] will do everyother from [1]->[5]
#[start:stop:stepover]
#this will print from [2] -> last element
print(str_1[2:])

#this will print from [0] -> [5]
print(str_1[:5])

#stepover, start at print[1] and [3] and [5]
#does not include stop location, if range is 0->5 it will not include 5 (at least here)
print(str_1[1:6:2])

#printing [-1] will take the last element in the list, [-2] is the second last element
print(str_1[-1])

#Print string REVERSE
print(str_1[::-1])

#entire list
print(str_1[:])

#[start, stop, increment]