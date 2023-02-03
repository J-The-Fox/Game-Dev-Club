"""
How to create a function in python!
"""

arg1 = "Orange"
arg2 = "White"

# A Triditional Argument, Or Positional Argument, Are Required Values, You Must Have Them Set Or An Excpetion Will Be Thrown
# A Key Word Argument Are Optional Values, You Do Not Need To Supply These. If No Value Is Supplied, They Go To A 'Default' Value
def my_function(arg1, arg2, kwarg1 = "Green"):
    """
    This Is A Test Function
    """
    # Adding The Double Apostrophes (") 3 Times Can Create A Block String, Add These At The Top Of A File Or Right After
    # A Function Declaration To Add A Description When You Hover Over It!
    # VS Code Will Use Markdown So You Can Use That In Your Descriptions. Keep In Mind That It Won't Work An Every IDE Though

    print(f"Here Is Arg 1: {arg1}, Arg 2: {arg2}, And Kwarg1: {kwarg1}!")

# This Function Is The Same As The First But Uses Types To Help Identify What To Pass In
# Notice How When You Hover Over It They Say 'str' Instead Of 'Any'. You Can Add Multiple By Adding The Type Followed By A '|' Then Another Type
# Like This: str | int or dict | list
def my_function_str(arg1: str, arg2: str, kwarg1: str = "Green"):
    """
    This Is Another Test Function
    """
    print(f"Here Is Arg 1: {arg1}, Arg 2: {arg2}, And Kwarg1: {kwarg1}!")


if __name__ == "__main__": # This Line Makes Sure That The File Can Only Be Called By Directly And Not Excuted By Another File, Helpful To Have When Importing Files
    my_function(arg1, arg2) # my_function with 2 arguments but not key word argument
    my_function(arg1, arg2, kwarg1="Yellow") # my_function with 2 arguments and a key word argument