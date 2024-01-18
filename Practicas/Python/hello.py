#Ask the user for their name
name = input("What's your name?")

#Remove whitespace frfom str
#name = name.strip()

#Converts the first letter of a string to uppercase and the rest to lowercase
# name = name.capitalize()

#Converts each word in a string to uppercase.
#name = name.title()

name = name.strip().title()

#The expression end="" is used in the print() function in Python to specify what will be printed at the end of the string being printed.
print("Hello, ", end="")  
print(name)

age = input("What's your age?")

#The "f" in Python is used in the creation of f-strings, which are format strings.
print(f"Hello {name}, you're {age} years old")

#Those aren't quotes that finish or start the thought, they're literal quotes.
print("Hello, \"friend\"")


