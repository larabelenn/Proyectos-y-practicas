#This function serves as the main entry point of the program.
def main():
    x = int(input("What's x?"))
    print("x squared is", square(x))
#The program calls the function square(x) to calculate the square of x.

#The variable n is a parameter used to represent the number that will be passed as an argument.
def square(n):
    return pow(n, 2)
#pow () It's a built-in function in Python used to raise a number to a power.   
#The first argument, `n`, is the base, and the second argument, 2, is the exponent.

main()







