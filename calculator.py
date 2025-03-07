#enter numbers
x = float(input("First number: ").strip())
sign = (input("+, -, /, * : "))
y = float(input("Second number: ").strip())

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
if sign == "+": print("*",x,"+",y," =",(x+y))
if sign == "-": print("*",x,"-",y," =",(x-y))
if sign == "/": print("*",x,"/",y," =",(x/y))
if sign == "*": print("*",x,"*",y," =",(x*y))
