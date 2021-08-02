# x = 15
# y = 7

# if x > y:
#    print('yes')



  #  =====================

# x = 5
# y = 7

# if x < y:
#   print('No')

  #  ====================

# if 'Hello' in 'Hello world!':
#       print('Yes')

  #  ====================

x = 5
y = 7

# if x > y:
#    print('yes it is greater')
# elif x < y:
#    print('no it is less')
# else:
#    print('Neither')   

  #  ====================


'''
Nested if  Statements
'''

# num = 0

# if num >= 0:
#     if num == 0:
#        print("Zero")
#     else:
#        print("Positive number")
# else:
#   print("Negative number")

#  #  ====================

'''
one-line if statement
'''

# if 7 > 5: print('yes it is')

# ========================

'''
Ternary operator
'''

# print('Yes') if 7 > 5 else print('No')

# #  it is the same as:

# if 7 > 5:
#    print('Yes')
# else:
#    print('No')

# ========================

# if 100 > 50:
#    print('Yeah')



# cifra = 4.5

# if cifra <= 2:
#      if cifra == 2:
#        print('two')
#      else:
#        print('Incorrect')
# else: 
#    print('Correct')

'''
Python Crash Course
'''

# if statements

# age = 17
# if age >= 18:
#     print("You are old enough to vote!")


# age = 19
# if age >= 18:
#     print("You are old enough to vote")
#     print("Have you registred to vote yet")


# if-else Statement

# age = 17
# if age >= 18:
#     print("You are old enough to vote!")
# else:
#     print("You are too young to vote.")
#     print("Please, register to vote as soon as you turn 18.")    

# if-elif-else Chain

# age = 75

# if age < 4:
#     print("Your age admission fee is 0.")
# elif age < 18:
#       print("Your admission fee is $25.")
# else:
#       print("Your admission fee is $40.")    


#  Using Multiple elif Blocks


# age = 70 

# if age < 4:
#   price = 0
# elif age < 18:
#   price = 25
# elif age < 65:
#   price = 45
# else:
#   price = 20

# print(f"Your admission cost is ${price}.")

# Omitting the else Block

# age = 12 

# if age < 4:
#   price = 0
# elif age < 18:
#   price = 25
# elif age < 65:
#   price = 45
# elif age >=65:
#   price = 20    

# print(f"Your admission fee is ${price}.")


# Testing Multiple Conditions

# requested_toppings = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings:
#     print("add mushrooms")
# if 'peperoni' in requested_toppings:
#     print("add peperoni")
# if 'extra cheese' in requested_toppings:
#     print("add extra cheese")

# print("\nFinished making your pizza!")


#  Exercise. 5.3


# alien_colours = 'green'

# if alien_colours == "green":
#     print("you are getting 5 points")


 
# alien_colours = 'yellow'

# if alien_colours == 'green':
#     print("you are getting 5 points")

# else:
#     print("You are not winning anything, try one more time.")


# alien_colour = 'red'
# if alien_colour == 'green':
#   print("You are getting 5 points")
# else:
#   print("Try one more time")


#  Exerscise 5.4

# alien_colour = 'green'

# if alien_colour == 'green':
#     print("You jusr earned 5 points")
# else:
#     print("You just earned 10 points")

  # =======

# alien_colour = 'red'

# if alien_colour == 'green':
#     print("You jusr earned 5 points")
# else:
#     print("You just earned 10 points")


# alien_colour = 'red'

# if alien_colour == 'green':
#     print("You jusr earned 5 points")
# elif alien_colour == 'yellow':
#     print("You just earned 10 points")
# elif alien_colour == 'red':
#     print("You just earned 15 points")   


# ========

# alien_colour = 'green'

# if alien_colour == 'green':
#     print("You jusr earned 5 points")
# elif alien_colour == 'yellow':
#     print("You just earned 10 points")
# elif alien_colour == 'red':
#     print("You just earned 15 points")  

# =======


# alien_colour = 'yellow'

# if alien_colour == 'green':
#     print("You jusr earned 5 points")
# elif alien_colour == 'yellow':
#     print("You just earned 10 points")
# elif alien_colour == 'red':
#     print("You just earned 15 points")  


# ======

# alien_colour = ''

# if alien_colour == 'green':
#     print("You jusr earned 5 points")
# elif alien_colour == 'yellow':
#     print("You just earned 10 points")
# elif alien_colour == 'red':
#     print("You just earned 15 points")  
# else:
#     print("You have earned 1 point")

# ======== 5.5

# age = 15

# if age < 2:
#   person = 'baby'
# if age < 4:
#   person = 'toddler'
# if age < 13:
#   person = 'kid'
# if age < 20:
#   person = 'teenager'
# if age < 65:
#   person = 'adult'
# if age >= 65:
#   person = 'elder'

#   print(f"This person is a {person}.")

# age = 67 

# if age < 2:
#   print("this person is a baby")
# if age < 4:
#   print("this person is a toddler")
# if age < 13:
#    print("this person is a kid")
# if age < 20:
#    print("this person is a teenager")
# if age < 65:
#    print("this person is a adult")
# if age >= 65:
#    print("This person is an elder")



# ========= 5.7

# favourite_fruits = ['pears', 'strawberries', 'grapes', 'banana']
# if 'banana' in favourite_fruits:
#   print('banana'.title())
# if 'berries' in favourite_fruits:
#   print('berries'.title())
# if 'pears' in favourite_fruits:
#   print('pears'.title())
# if 'cucumber' in favourite_fruits:
#   print('cucumber'.title())
# if 'grapes' in favourite_fruits:
#   print('grapes'.title())

# print("\n These are some of my favourite fruits!")

# ======================================

# favorite_fruits = ['grapes', 'strawberries', 'peaches']

# if 'grapes' in favorite_fruits:
#     print("You really like grapes!")
# if 'apples' in favorite_fruits:
#     print("You really like apples!")
# if 'strawberries' in favorite_fruits:
#     print("You really like strawberries!")
# if 'bananas' in favorite_fruits:
#     print("You really like bananas!")
# if 'peaches' in favorite_fruits:
#     print("You really like peaches!")

# ====================================


'''
Using If Statement with a list
'''

#  1. Checking for special items 

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#     print(f"Adding {requested_topping}.")

# print("\nThat pizza is ready to be served")

#  => if the pizzeria though runs out of green peppere, here is how the code will look like

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for topping in requested_toppings:
#   if topping == 'green peppers':
#     print("Sorry, we run out of green peppers at the moment")
#   else:
#     print(f"Adding {topping}!")

# print("\nThat pizza is ready to be served!")

#  2. Checking that a list is not empty

# requested_toppings = []

# if requested_toppings:
#   for requested_topping in requested_toppings:
#     print(f"Adding {requested_topping}.")
#   print("\nFinished making your pizza")
# else:
#   print("Are you sure you want a plain pizza?")

# =====

# requested_toppings = ["peppers"]

# if requested_toppings:
#   for requested_topping in requested_toppings:
#     print(f"Adding {requested_topping}.")
#   print("\nFinished making your pizza")
# else:
#   print("Are you sure you want a plain pizza?")


#  3. Using Multiple Lists

# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for requested_topping in requested_toppings:
#   if requested_topping in available_toppings:
#     print(f"Add {requested_topping}.")
#   else:
#     print(f"Sorry, we do not have {requested_topping}.")
  

# print("\nFinished making your pizza")


# ==== Exercises

# 5.8

# users_list = ['john', 'peter', 'marina', 'admin', 'stella', 'sandra']

# for user in users_list:
#   if user == 'admin'.title():
#     print("Hello admin , would you like to see a status report?")
#   else:
#     print(f"Hello {user.title()}, thank you for loggin in again!")


# 5.9

# users_list = ['john', 'peter', 'marina', 'admin', 'stella', 'ema']

# if users_list:
#   for user in users_list:
#    if user == 'admin'.title():
#       print("Hello admin , would you like to see a status report?")
#    else:
#       print(f"Hello {user.title()}, thank you for loggin in again!")

# else:
#   print("We need to find some users")

# 5.10
