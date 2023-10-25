# Built-In Modules
import random

# This Is A Try, Except Block
# This Will Try To Run The Code In The Try Block
try:
    # This Will Throw An Error Because You Can't Divide By Zero
    print(1/0)
# This Will Catch The Error And Run Code Placed Here
# Using Except Without A Specific Error Will Catch Any Error
except:
    print("There Was An Error")

# You Can Also Catch Specific Errors
try:
    # This Will Throw An Error
    print(1/0)
# This Will Catch The Error
except ZeroDivisionError:
    print("There Was A Zero Division Error")

# You Can Also Catch Multiple Errors
try:
    print(1/0)
except (ZeroDivisionError, TypeError):
    print("There Was An Error")

# If You Want To Catch Different Errors You Can Use Multiple Except Blocks
try:
    # This Will Throw An Error
    if random.random() > 0.5: # Will Pick At Random, Either 1/0 Or "Hello World!" + 1. Each Will Throw A Different Error
        print(1/0)
    else:
        print("Hello World!" + 1)
except ZeroDivisionError:
    print("There Was A Zero Division Error")
except TypeError:
    print("There Was A Type Error")

# You Can Also Use Else And Finally
try:
    if random.random() > 0.5:
        print(1/0)
    else:
        print("Hello World!")
except:
    print("There Was An Error")
else:
    print("There Was No Error")