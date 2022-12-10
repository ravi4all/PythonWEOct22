a = 23
b = 21
c = a + b
d = a / b

print(c)
print("Sum is",c)
print("Sum of",a,"and",b,"is",c)

#print("Sum is %f"%c)

print("Sum is {}".format(c))
print("Div is {}".format(d))
print("Div is {:.2f}".format(d))

print("Sum of {} and {} is {}".format(a,b,c))
print("Sum of {2} and {0} is {1}".format(b,c,a))

#f-string
print(f"Sum of {a} and {b} is {c}")
print(f"Div of {a} and {b} is {d:.2f}")









