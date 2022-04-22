#Function: Functions are the block of stmts which perform particular task.
#-Fucntion are not executed automatically
#-To execute functions, we need to make a function call.
#-We can make 'n' number of function calls.
#-Functions are executed on demand by making a call.
#-Function are define by using keyword ---> def.
#- All the stats within function should follow the indentattion
#- syntax for defining  a function :
from ast import stmt


def functionname(arguments):
    """Document String"""
    stmt1
    stmt2
    stmt3
    stmt4
    return stmt

#-> Docstring specifies the functioanlity of a function .i.e what is the function meant forspecifying document string is optional.
def display():                   #Function definition
    """sample function to display a message"""
    print("Hello......")
    print("Good Morning......")

display()                        #Function call
