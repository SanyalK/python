#Accepting Dictionary keys and Dictionary values from the user Keyboard
#Converting a list to Dictionary#Merging 2 lists ---> Using zip function and later convert to Dictionary
from multiprocessing.sharedctypes import Value

from pygtkcompat import enable_goocanvas


subjects=[]
marks=[]


print("Enter the Subjetc Names as keys: ")
for p in range(1,6):
    key=input("Enter the name of Subjects"+ str(p)+":")
    subjects.append(key)
print(subjects)

print("Enter the subjetc marks as values: ")
for p in range(0,5):
    key=int(input("Enter the marks of "+ subjects[p]+": "))
    marks.append(key)
print(marks)

#Merging the 2 lists using zip() function
x=zip(subjects,marks)
print(x,type(x))


y=list(x)
print(y,type(y))

z=dict(y)
print(z,type(z))