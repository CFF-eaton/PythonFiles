def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b


print("Choose an operation:")
print("1 addition")
print("2 subtraction")
a=int(input("Enter Choice:"))
num1=int(input("Enter first num"))
num2=int(input("Enter second num"))
if a==1:
    print("Result"+addition(num1,num2))
else:
    print("Result"+subtraction(num1,num2))
    