#Accepting tuple of Values from the Usr keyboard
print("Enter the marks of 5 Subjects : ")
y=tuple(int(p) for p in input().split(" "))
print(y,type(y))
