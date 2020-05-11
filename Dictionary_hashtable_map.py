#Dictionary
#creats a key and value pair, you define a key for each value pair, unordered list (not next to each other in memory).

#dictionaries can hold multiple data types boolean, array, string, float, ect..
dictionary = {
    'a' : 123,
    'b' : 456,
    'cee' : "see",
    'my_array': [1,2,3,4,5,6]
}

print(dictionary['a'])
print(dictionary['my_array'][1])#gets a index value from the 'my_array' key

#LIST, can contain dictionaries too (any data structure)
my_list = [{
    'a' : 123,
    'b' : 456,
    'cee' : "see",
    'my_array': [1,2,3,4,5,6]
},
    {
    'a' : 321,
    'b' : 654,
    'cee' : "see",
    'my_array': [1,2,3,4,5,6]
}]
print(my_list)#prints all
print(my_list[1]['my_array'][0])#[first item in list] (i.e. between first { }, [what_item_in_list][key][index]


#KEYS can be ints and other types too, making a list with dictionary in it to hold multiple data types, keys MUST be unique, or else will overwrite it on second call
new_keys = {
    123 : 'password correct',
    456 : 'password incorrect',
    'admin':'access_granted'
}

print(new_keys[123])
print(new_keys[456])
print(new_keys['admin'])#90% a string tho


#if a key does not exist it will give an error, can use new_keys.get('search_for', if_not_there_use_this_value)

print(new_keys.get('add'))
print(new_keys.get('add', 20))#will call 20 since it does not exist but will NOT save the key
print(new_keys)

#can use built in function (less common)
user2 = dict(name = 'john')#no ' 'string wrap needed
print(user2)

#error prevent, can use 'in' to check if value is in list or dictionary same as .get
print('none' in new_keys)#is 'none' in new_keys?
print('password correct' in new_keys)#only checks keys can use .values to check for values
print(123 in new_keys)#key does exist


#can look up dictionary methods on google
#new_keys.values() can check the values
#new_keys.keys to seach for keys
new_keys = {
    123 : 'password correct',
    456 : 'password incorrect',
    'admin':'access_granted',
    'age' : 20
}
print(123 in new_keys.keys())#True, is a key
print(654 in new_keys.keys())#False, no key
print('password correct' in new_keys.keys())#false no key called that
print('password correct' in new_keys.values())#true, is a value called that

#items, prints all items
print(new_keys.items())

#Clear dictionary
new_keys.clear()
print(new_keys)#empty now

#Copy a user
new_keys = {
    123 : 'password correct',
    456 : 'password incorrect',
    'admin':'access_granted',
    'age' : 20
}
new_keys2 = new_keys.copy()
print(new_keys)
print(new_keys2)
new_keys.clear()
print(new_keys)#empty
print(new_keys2)#full still

#.pop('key_to_delete') will return the key if returned on assignment
new_keys2.pop('age')#delete 'age' key and its value
print(user2)#'age' and value deleted

#popitem removes some pair, not always the last one
new_keys = {
    123 : 'password correct',
    456 : 'password incorrect',
    'admin':'access_granted',
    'age' : 20
}
new_keys.popitem()
print(new_keys)

#update, updates key to a new value, if the key doesnt exist, will ADD to the dictionary list, remember the { }
new_keys.update({123 : "changed"})
print(new_keys)
new_keys.update({112233 : "created from .update"})#added a new key pair
print(new_keys)
