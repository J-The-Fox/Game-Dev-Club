class my_class():
    """
    A New Class Called my_class!
    """

    def __init__(self, arg1, arg2, kwarg1 = "Green"):
        self.argument1 = arg1
        self.argument2 = arg2
        self.key_word_argument1 = kwarg1
    # This Is The '__init__' Method In A Class, This Can Be Created To Grab
    # Arguments And Keyword Arguements. 
    # Notice The 'self' Parameter. This Is How Classes Can Be Assigned To Varaibles
    # When 'my_class_variable' Gets Assigned To 'my_class()', The 'self' Is Now 'my_class_variable'!
    # Pretty Neat.
    #
    # The '__init__' Method Runs The First Time That Class Is Assigned Then Never Again
    # Useful For Setting Stuff Up

    def my_method(self):
        print("In 'my_method'!")
    # A Method Inside This Class
        
    def print_args(self):
        print(f"Here Is Arg 1: {self.argument1}, Arg 2: {self.argument2}, And Kwarg1: {self.key_word_argument1}!")

my_class_variable = my_class(arg1="Orange", arg2="White")
# Asigning 'my_class' To 'my_class_variable'
# The 'my_class_variable' Is Now 'self'

my_class_variable.my_method()
my_class_variable.print_args()
# You Can Use Methods Just Like Functions, With Arguments And Key Word Arguments
# None Have Arguments Here Besides The '__init__'

my_class_variable = my_class(arg1="Orange", arg2="White", kwarg1="Yellow")
# Asigning 'my_class' To 'my_class_variable' Except With Keyword Arguments

my_class_variable.print_args()
# Running 'print_args'