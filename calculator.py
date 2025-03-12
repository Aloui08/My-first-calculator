print(" ")
print(" ")
print("         1      2      3")
print(" ")
print(" ")
print("         4      5      6")
print(" ")
print(" ")
print("         7      8      9")
print(" ")
print(" ")

# Get user input
x = int(input("First Number? ").strip())
print(" ")
sign = input("+, -, *, /: ").strip()
print(" ")
y = int(input("Second Number? ").strip())

# Function to perform the first calculation
def maram(x, sign, y):
    if sign == "+":
        return x + y
    elif sign == "-":
        return x - y
    elif sign == "/":
        return x / y
    elif sign == "*":
        return x * y
    else:
        return "Invalid operator"

# Store the result of maram
maramresult = maram(x, sign, y)
print(" ")
print(f"{x} {sign} {y} = {maramresult}")

# Get second input for second calculation
print(" ")
sign2 = input("+, -, *, /: ").strip()
print(" ")
z = int(input("Third Nuùber? ").strip())

# Function to perform the second calculation using maram's result
def ka7la(maramresult, sign2, z):
    if sign2 == "+":
        return maramresult + z
    elif sign2 == "-":
        return maramresult - z
    elif sign2 == "/":
        return maramresult / z
    elif sign2 == "*":
        return maramresult * z
    else:
        return "Invalid operator"

# Store the result of ka7la and print the second calculation
ka7laresult = ka7la(maramresult, sign2, z)
print(" ")
print(f"{maramresult} {sign2} {z} = {ka7laresult}")

#Get third input for third calculation
print(" ")
sign3 = input("+, -, *, /: ").strip()
print(" ")
f = int(input("Forth Number? ").strip())

# Function to perform the third calculation using ka7la's result
def salim(ka7laresult, sign3, f):
    if sign3 == "+":
        return ka7laresult + f
    elif sign3 == "-":
        return ka7laresult - f
    elif sign3 == "/":
        return ka7laresult / f
    elif sign3 == "*":
        return ka7laresult * f
    else:
        return "Invalid operator"

# Store the result of ka7la and print the final calculation
finalresult = salim (ka7laresult, sign3, f)
print(" ")
print(f"{ka7laresult} {sign2} {f} = {finalresult}")