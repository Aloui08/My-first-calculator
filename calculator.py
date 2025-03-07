#enter numbers
x = int(input("First number: ").strip())
sign = (input("+, -, /, * : "))
y = int(input("Second number: ").strip())

#space
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")

#resultat
print("#resultat :")
print(" ")
if sign == "+": print("*",x,"+",y," =",int(x+y))
if sign == "-": print("*",x,"-",y," =",int(x-y))
if sign == "/": print("*",x,"/",y," =",int(x/y))
if sign == "*": print("*",x,"*",y," =",int(x*y))