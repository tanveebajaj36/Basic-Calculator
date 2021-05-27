print("Basic Calculator")

num1 = input("First Number: ")
operation = input("Add Operator: ")
num2 = input("Second Number: ")

if("+" in operation):
    print(str(int(num1) + int(num2)))
elif("-" in operation):
    print(str(int(num1) - int(num2)))
elif("x" in operation):
    print(str(int(num1) * int(num2)))
elif("/" in operation):
    print(str(int(num1) / int(num2)))
else:
    print("Operation not found")