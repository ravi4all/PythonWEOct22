# **kwargs - variable length keyword argument
# def person(**details):
#     print(details)
#
# person(id=101, name="Ram")
# person(name="Shyam", salary=45000, age=20, dept="IT")

# def person(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# person(101, "John")
# person(id=101, name="Shyam")

def person(id, name, *args, **kwargs):
    pass

person(101, "John")
