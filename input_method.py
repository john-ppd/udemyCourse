#inputs are strings, must wrap with int to use in math

is_int = input("input a number, ill add one to it" * 3)
print(type(is_int))
print(int(is_int) + 1)

#using f string
birth_year = int(input("what year were you born?"))
users_age = 2020 - birth_year
print("wow, you're " + str(users_age) + " years old!!!")

#fstring
print(f"wow, youre {users_age} years old!!!")