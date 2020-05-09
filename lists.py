#lists are like arrays in other languages
#lists are data structures
list_1 = [1,2,3,4,5]
list_2 = [
    "shampoo",
    "notebooks",
    "apple",
    "another4",
    "another5"
]
list_3 = [True, "string", 5]

print (list_3[:])#will print entire list

#list slicing
#[start:<than:interval]
print(list_2[0:2:1])

#CAUTION -- when assigning a variable to a list, we have to use l = l1[:] or else it will store the memory location of l1 and any change in either will change both since its referencing memory, use l = l1[:] to make a new copy

l = list_1
print(l)
print(list_1)

l[0] = "apple"
print(l)
print(list_1)#change was applied to both

l = list_1[:]
l[0] = "orange"
print(l)#changed
print(list_1)#didn't change