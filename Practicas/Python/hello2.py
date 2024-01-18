#Functions are reusable blocks of code that perform a specific task when called.
#The parameter `to` acts as a placeholder that will receive the value you pass when you call the function.
def hello(to="world"):
    print ("hello,", to)

#If you don't provide a name, it will print 'Hello, world'

hello()
name = input("What's your name?")
hello (name)