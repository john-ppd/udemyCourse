#len(var_1) will start at 1 and count the length of the object
greet = "hellloooo"
print(len(greet))
#[start:stop location]
print(greet[0:len(greet)])

#look up string built in methods and you will find built in methods that only work for strings, usually has a . so is a class
print(greet.isupper())
#if you dont assign it but use it the change will not save
greet = greet.upper()
print(greet.isupper())
#capitalize the first letter
greet = greet.lower()
print(greet.capitalize())
#find something within a string, will return the starting index location
print(greet.find("el"))
#replace all somethings for something else
print(greet.replace("el","hi"))