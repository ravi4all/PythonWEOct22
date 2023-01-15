# Positional Argument
# def greet(fname, lname):
#     print("Hello",fname, lname)

# Default Argument
def greet(fname, lname=""):
    print("Hello",fname, lname)

# greet()
# greet("Ram")
# greet("Ram", "Sharma")

# Keyword Argument
# greet(fname="Ram", lname="Sharma")
# greet(lname="Sharma", fname="Ram")

greet("Ram")
greet("Ram", "Sharma")
greet(fname="Ram")

