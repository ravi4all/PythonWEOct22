# Global Variable
name = "Gopal"

# Function Definition
def greet():
    # Local Variable
    # name = "Ram"
    # global keword - converts local variable into global variable
    global name
    name = "Ram"
    print(f"Hello {name}...")


# Function Call
greet()
print("Hello",name)
