# first = input("Enter your first name: ")
# last = input("Enter your last name: ")
# username = first[:3].lower() + last[-3:].lower()
# print("Suggested Username:", username)


# first = input("Enter your first name: ")
# last = input("Enter your last name: ")
# username = first[:3].lower() + last[3:].lower()
# print("Suggested Username:", username)     



 
import random
first = input("First name: ")
last = input("Last name: ")
number = random.randint(000, 9999)
username = first[:3].lower() + last[-3:].lower() + str(number)
print(username)