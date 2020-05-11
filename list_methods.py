#if you hover over the .method() you will see the return type just right of -->, if --> None, then cannot be assigned to a variable because doesn't return anything

#find lenth of list
basket = [1,2,3,4,5]

#append, if you set basket = basket.append(6) it will return as NONE because the action only modified the list in place, did not create a value, its to be used by itself
basket.append(6)
print(basket)

#list length len()
print(len(basket)) # 6 elements

#inserting into a list
#list.insert(what_memory_location, what_value)

basket.insert(1, 100)#at[1] insert 100, shift right
print(basket)


#removing
#remove last item list.pop()
print("before .pop " + str(basket))
basket.pop()
print("after .pop " + str(basket))

#remove item at an index .pop(index_location), will also return what it just removed if assigned to a var
basket.pop(0)#will remove [0]
print(print("after .pop(0) " + str(basket))
)

#search and remove a value if found
basket.remove(100)
print("after .remove(100) " + str(basket))

#clear all, list.clear()
basket.clear()
print("after .clear() " + str(basket))

#find index of a value within a list
#list.index(value) searches for the value in the list and returns the index location

basket = [1,2,3,4,5,"six"]#each location will keep its vaible type
print(basket.index(2)) # returns 1 because is value at [1]

print(type(basket[5]))

#to check if something is in list, better for avoiding errors
print(3 in basket)#is 3 in basket list, True
print("n" in basket)#is 'n' in basket? False

#count how many of searching value is in
basket.append(3)
basket.append(3)
basket.append(3)
basket.append(3)
basket.append(3)
print(basket)
print(basket.count(3))#how many 3's are in our list?

#SORT list a-z or 0-9
print(basket)
basket.remove("six")#had to remove the string in it for sort
basket.sort()
print(basket)

#to just print sorted list but not create new one, used to assign a list to another list in seperate memory locations, can use basket_2 = basket[:], or basket_2 = basket.copy() too
basket = [2,1,3,4,5]

print(sorted(basket))#just copied
print(basket)#not changed

basket_2 = sorted(basket)
basket_2.append("appended")
print("Basket")
print(basket)
print("Basket 2")
print(basket_2)

#highest to lowest, sort and then reverse
print(basket)
basket.sort()
print(basket)
basket.reverse()
print(basket)


#extend seems to be the same as append but an add multiple to end, be careful, must use .extend([elemets_to_add, , ])
basket.extend([100,101,102])
print(basket)


print(basket.index(101))#returns the index location of value 101 in our list, in this case its 6 for basket[6]
print(basket[6])

#search within set range .index(search_for, start_at_[], stop_one_before_[])
print(basket.index(101,1,7))


#keywords, search for python3 keywords
#'in' keyword will return True if a value you look for is 'in' some list, better to check before search, if True, search. For Error minimalizing

print(101 in basket)#True because value of 101 is in basket list
print("test" in basket) #False because "test" is not in basket

#count amount of values occur in list
basket.insert(3,99)#@[3] insert 99, shift right
basket.append(3)
basket.sort()
print(basket)
print(basket.count('not_there'))
print(basket.count(3))#there are 2 #3's in list

#Reverse order without sorting
print("pre reverse")
print(basket_2)
print("post reverse")
basket_2.reverse()#if in print will return None
print(basket_2)


#copy  list to other list
list_1 = ['hi', 'there', 'john']
list_2 = list_1.copy() #need to use copy for seperate memory location
list_2.append("d")
print(list_1)
print(list_2)

#List slicing reverse list
list_3 = list_2[::-1]#new memory copy
list_3.append("appended")
print(list_3)
print(list_2)


#create list with range
list_range = list(range(0,100)) #will create a list with values 0-99 in [0] - [99]
print(list_range)


#joining list items with some sort of character or space
sentence = ' ! '#will alternate being inserted into new list
sentence_join = sentence.join(['this','is','a','sentence','joined','together'])
print(sentence_join)
print(sentence_join.index(' ! '))
print(sentence_join.count(' ! '))

#join strings, lazy way
sentence = ' '.join(['this','is','a','sentence','joined','together'])#will put a space between each entry that will take up a memory location, can be any variable, not just ' '
print(sentence)
print(sentence.index(" "))#where first space is
print(sentence.count(" "))


#LIST UNPACKING, assigning multiple variables using a list in one line of code
print("list unpacking")
a,b,c = [1,2,3]
print(a)
print(b)
print(c)
print(a+b+c)

#can make more items than variables with no error
print("list unpacking, * method")
a,b,c,*d = [1,2,3,4,5,6] #d will be assigned remaining items
print(a)
print(b)
print(c)
print(d)

a,b,c,*d,e = [1,2,3,4,5,6,7,8,9] #*d will be assigned remaining items EXCEPT LAST ITEM, that is assigned to e
print(a)
print(b)
print(c)
print(d)
print(e)


