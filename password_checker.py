#task is to display * and how many letters long a password is
user_name = input("type username : ")
password = input("type password : ")

print(f"hi {user_name}, your password is {'*' * len(password)} and is {len(password)} digits long")