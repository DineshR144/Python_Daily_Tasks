print("1.ADD")
print("2.SUB")
print("3.MUL")
print("4.div")
print("5.MOD")
c = int (input("Enter your option:"))
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def mod(a, b):
    return a % b
if c == 1:
    ans = add(a, b)
elif c == 2:
    ans = sub(a, b)
elif c == 3:
    ans = mul(a, b)
elif c == 4:
    ans = div(a, b)
elif c == 5:
    ans = mod(a, b)
else:
    ans = "Invalid option"

print("Result:", ans)

