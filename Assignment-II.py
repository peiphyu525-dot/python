# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 20:48:59 2026

@author: Double Y
"""

a=int(input("This is the first number:"))
b=int(input("This is the second number:"))
c=input("Choose function(+,-,*,/):")

all_a=id(a)
all_b=id(b)
print("The allocation of a is",all_a)
print("The allocation of b is",all_b)
print("Hex of a is",hex(a))
print("Hex of b is",hex(b))

def addition(x,y):
    print(x+y)
    
def subtraction(x,y):
    print(x-y)
    
def division(x,y):
    print(x/y)
    
def multiplication(x,y):
    print(x*y)
    
    
if c == "+":
    addition(a,b)
    
elif c == "-":
    if a>b:
       subtraction(a,b)
    elif b>a:
        subtraction(b,a)
        
elif c == "/":
    if b != 0:
       division(a,b)
    else:
        print("Cannot divide by zero")
        
elif c == "*":
    multiplication(a,b)
    
else : print("Invalid function")

        
        