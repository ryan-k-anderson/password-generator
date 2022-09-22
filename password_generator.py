import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','#','$','&','(',')','*','+']

# Introduction to the Password Program
print("Welcome to the PyPassword Generator")

nr_letters = int(input(f"How many letters would you like to have? \n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like? \n"))
# All inputs will be converted to an integer

password = []
for letter in range(1, nr_letters+1):
    password.append(letters[random.randint(0,52)])
# print(password)

for symbol in range(1, nr_symbols+1):
    password.append(symbols[random.randint(0,7)])

for number in range(1, nr_numbers+1):
    password.append(numbers[random.randint(0,9)])

new_password=''
for x in password:
    new_password += '' + x
print(''.join(random.sample(new_password, len(new_password))))

