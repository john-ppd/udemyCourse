#a long string can be created by using ''' "user text" '''
#long string can go on multiple lines

long_string = '''
T
es
   t
'''
print(long_string)

#combining strings
string_1 = "john "
string_2 = "sev"

string_3 = string_1 + string_2
print(string_3)

#combining string and int
string_1 = "john "
int_1 = 3
combine_int_str = string_1 + str(int_1)
print(combine_int_str)
print(type(combine_int_str))

#If we use \ within quotes it will take the next variable as a string even if its " or \
#\n is new line
#\t is tab


weather = "\ts\"u\\nn\ny"
print(weather)