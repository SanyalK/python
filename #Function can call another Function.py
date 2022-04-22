#Function can call another Function
def hyd():
    print("Hello Hyderabad")

def pune():
    print("Hello Pune")


def delhi():
    print("Delhi say\n")
    hyd()
    pune()

delhi()
