#set is a data structure that is an unordered collections of unique objects

my_set = {1,2,3,4,5,5}#this is a set
print(my_set)#only prints 5 once because it is only unique values, will not add a duplicate

#task, remove duplicates from an array
my_list = [1,1,2,3,3,4,5,6,6,7,7]
my_set = my_list.copy()#will break the rule and add multiples
print(my_set)#has multiples
my_set = set(my_list.copy())#needs set(wrap)
print(my_set)#works when wrapped

#sets do not support idex calls, more like a dictionay, will have to make into a list again

my_list = list(my_set)
print(my_list)
print(my_list[1])

#.difference, when viewed from what, what is in one and not in 2?
set1 = {1,2,3,4,5}
set2 = {4,5,6,7}
print(set1.difference(set2)) # 1,2,3 are in 1 but not in 2 so will print {1,2,3}
#discard a targetted value
print(set1)
set1.discard(1)#will delete value 1 from memeory
print(set1)

#difference update, same as difference but also deletes everything else other than return values
set1 = {1,2,3,4,5}
set2 = {4,5,6,7}
set1.difference_update(set2)
print(set1)#updates to a new set with only unique values from 1 onto 2


#intersection, if two sets have the same value stored in an index it will return all duplicate values
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7}
print(set1.intersection(set2))#prints 4,5,6 because they are in both sets
set3 = set1 & set2#shortcut for set3 = set1.intersection(set2)
print(set3)


#.isdisjoing, boolean for if set are all unique values, any duplicates will return false
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7}
print(set1.isdisjoint(set2))#False, there are dupes
set1 = {1,2,3,4,5}
set2 = {6,7,8,9}
print(set1.isdisjoint(set2))#True, no dupes


#.union unites sets togther into a net set and removes duplicates
set1 = {1,2,3,4,5}
set2 = {5,6,7,8,9}
set3 = set1.union(set2)
print(set3)#removed duplicate 5's
set3.clear()
set3 = set1 | set2#is shortcut for set3 = set1.union(set2)
print(set3)


#.issubset, are ALL values of set1 within set2?
set1 = {1,2,3,4,5}
set2 = {5,6,7,8,9}
print(set1.issubset(set2))#False

set1 = {3,4,5}
set2 = {3,4,5,6,7,8,9}
print(set1.issubset(set2))#True, ALL values from set1 are within set2

#.issuperset, oppisite of issubset, so would check if all set2 is in set1
set1 = {3,4,5}
set2 = {3,4,5,6,7,8,9}
print(set1.issuperset(set2))#false, not all of set2 valuse are within set1
print(set2.issuperset(set1))#True, all valuse of set1 are within set2


