#tuple cannot have their value changed, a lot like lists, except for that
#tuple is faster than lists in memory
#tuple is list that are immutable or that cannot change

my_tuple = (1,2,3,4,5)#cannot change index values

#printing individual indexes does work
print(my_tuple[1])#prints '2'

print(5 in my_tuple)#does 5 exist in my_tuple? True

#tuples are valid keys in dictionaries
d = {
    123 : 'test1',
    345: 'test 2',
    (123, 456) : "tuple_key"
}

print(d[(123, 456)])#works as key

#can slice tuple
my_tuple = [1,2,3,4,5]
new_tuple = my_tuple[1:2]#copy [1]
print(new_tuple)#if 1 element only is in tuple with have 'element',

new_tuple = my_tuple[1:3]
print(new_tuple)#copies [1,2]

x= my_tuple[0]
y = my_tuple[1]
print(x)
print(y)

#can use one line code too
x, y ,z ,*other = [1,2,3,4,5,6,7,7]#same as lists
print(x)
print(y)
print(z)
print(other)
print(len(other))
print("index at value = 7 in *other")
print(other.index(7))
print(other.count(7))#how many 7's? this is 2











