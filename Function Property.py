#Function Property

#1. A function can be called for multiple times

def display():
    print("Good Morning")

display()

print("Hello how are you Ravi")
display()

#Advantage of using function :- Code re-usability
#The order in which the functions are defined and the order in which they are called.
# need not be the same

def English():
    print("ABCDEFGHI...........XYZ")

def Maths():
    print("12345......100")

def Physics():
    print("alpha,beta........")

Physics()
English()
Maths()
