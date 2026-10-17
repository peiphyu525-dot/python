
x=int(input("This is the first number:"))
y=int(input("This is the second number:"))

all_x=id(x)
all_y=id(y)
print(all_x)
print(all_y)

print("Addition=",x+y)
print("Multiplication=",x*y)
if x>y:
    print("Subtraction",x-y)
    print("Division",x/y)

elif y>x:
    print("Subtraction",y-x)
    print("Division",y/x)
    
