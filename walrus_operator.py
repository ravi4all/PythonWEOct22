a = 3
b = 21
#walrus operator
#print("Sum is",c := a + b)
#print(f"Sum is {(c := a + b)}")

print(f"""
Sum is {(c := a + b)}
Sub is {(d := a - b)}
Div is {(e := a / b):.2f}
Mul is {(f := a * b)}
""")
