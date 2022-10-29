a = 5
b = 6

# walrus operator :=
#print("Sum is",c := a + b)

#print(f"Sum of {a} and {b} is {(c := a + b)}")

# Multi-line Print
print(f"""
Sum is {(c := a + b)}
Sub is {(d := a - b)}
Div is {(e := a / b):.2f}
Mul is {(f := a * b)}
""")
