#usually called an f string

#By putting the f in front print (f"text") we can use {varname} within the string and don't have to wrap anything

str_1 = "john"
int_1 = 4

#old way
print("hi " + str_1 + " you are " + str(int_1))

#python 2 way, can give values to {} to prioritize what oder that your elements in the format bracet will fill them
#example, to print str_1 into second {} and int_1 in first
print("hi {1} you are {0}".format(str_1, int_1))
print("hi {} you are {}".format(str_1, int_1))
#if you create variable within the format brackets you need to call it directly into {}
print("hi {str_2} you are {int_2}".format(str_2 = "testing", int_2 = 1232))


#new way with python3
print(f"hi {str_1} you are {int_1}")