def calc():
    x, y = 21, 10

    def add():
        z = x + y
        return z

    def sub():
        z = x - y
        return z
    return add, sub

# a will hold reference of add function
# b will hold reference of sub function
a,b = calc()
a()     # it will call add function
b()     # it will call sub function

