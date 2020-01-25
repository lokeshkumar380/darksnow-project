import math
# name = input("Whats your Name ? ")
# color = input("What your color ? ")
# print(name+' likes '+color)

# birth_year = input('enter your birth year: ')
# age = 2019 - int(birth_year)
# print(age)
# course = "lokesh"
# print(course.__contains__("l"))

# first = 'John'
# last = 'Smith'

# msg = first +' '+ last +' is a coder'
# message = f'{first} {last} is a coder'
# print(message)

#print(' ' in first)
# print(math.factorial(5))
# print(math.sqrt(9))

# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It's a hot day")
#     print('Drink plenty of water')
# elif is_cold:
#     print("Its's a cold day")
#     print('wear warm clothes')
# else:
#     print("Its a lovely day")
# print('Enjoy the day')

# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)g : ')
#
# if unit.upper() == 'L':
#     converted = weight * 0.45
#     print(f'You are {converted} Kilos')
# else:
#     converted = weight / 0.45
#     print(f'You are {converted} Pounds')

# guessing game code starts---------------

# secret_number = 9
# guess_limit = 3
# guess_count = 0
#
# while guess_count < guess_limit:
#     guess_number = int(input('Guess :'))
#     guess_count += 1
#     if guess_number == secret_number:
#         print("You won!")
#         break
# else:
#     print("Sorry, You failed!")

# command = ""
# started = False
# while True:
#     command = input('> ').lower()
#     if command == 'start':
#         if started:
#             print("Car is already started")
#         else:
#             started = True
#             print("Car started ...")
#
#     elif command == 'stop':
#         if not started:
#             print(" Car is already stopped")
#         else:
#             started = False
#             print(" Car Stopped...")
#
#     elif command == 'quit':
#         break
#     else:
#         print("""
# only below commands we followed mind your commands
# start -- to start the car
# stop == to stop the car
# quit == to quit out of program
#         """)


# numbers = [1, 1, 1, 1, 10]
# for number in numbers:
#     output = ''
#     for count in range(number):
#         output += 'x'
#     print(output)

# numbers = [3, 5, 13, 8, 1]
# largest = 0
# for item in numbers:
#     if largest < item:
#         largest = item
# print(f'Largest item in list is : {largest}')

# using dictionaries
# phone = input("Phone: ")
# digits_mappings = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four"
# }
# output = ""
# for ch in phone:
#     output += digits_mappings.get(ch, "!") + "  "
#
# print(output)

# message = input(">")
# # words = message.split()
# # emoj_mapping = {
# #  ":)": "😁",
# #  "(:": "😢"
# # }
# # output = ""
# # for word in words:
# #     output += emoj_mapping.get(word, word)
# # print(output)

# import converter
# from converter import module_test, Dice
#
# dice = Dice()
# print(dice.roll())
# print(dice.roll().count(2))

# from pathlib import Path
#
# path = Path()
# for file in path.glob("*.py"):
#     print(file)