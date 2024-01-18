x = int(input("What's x?"))
y = int(input("What's y?"))

#z = int(x) + int(y)
z = x + y

print(z)

a = float(input("What's a?"))
b = float(input("What's b?"))

# round = (number[, ndigits])
c = round (a + b)

#The use of ":," indicates that the number should be formatted with commas as thousands separators
print(f"{c:,}")

#print(f"{c:.2f}")
#Indicates that I want to display the result with two decimal places.
