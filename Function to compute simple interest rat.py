#Function to compute simple interest rate

def compute():
    p=int(input("Enter the principal amount: "))
    t=float(input("Enter the time period": ))
    r=float(input("Enter the rate of interest: "))
    si=(p*t*r)/100
    print("Simple Interest Percentage is ",si)
compute()

