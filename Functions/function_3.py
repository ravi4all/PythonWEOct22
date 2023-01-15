# *args - variable length argument / arbitrary arguments
def sum(*x):
    # print(x)
    s = 0
    for i in x:
        s += i
    print("Sum is",s)

sum(4,5)
sum(4,4,3)
sum()
sum(7)
sum(3,5,8,3,5,8,4)
