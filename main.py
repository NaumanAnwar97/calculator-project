#!/usr/bin/env python
# coding: utf-8

# In[1]:


from calculator.add import add
from calculator.mul import mul
from calculator.div import div

def main():
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Choose operation (add/mul/div): ")

    if op == "add":
        print("Result:", add(a, b))
    elif op == "mul":
        print("Result:", mul(a, b))
    elif op == "div":
        try:
            print("Result:", div(a, b))
        except ValueError as e:
            print("Error:", e)
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()

