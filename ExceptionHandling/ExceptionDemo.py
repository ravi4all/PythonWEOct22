try:
    fnum = int(input("Enter first num : "))
    snum = int(input("Enter second num : "))
    a = fnum + snum
    print("Sum is",a)
    b = fnum - snum
    print("Sub is",b)
    c = fnum / snum
    print("Div is",c)
    d = fnum * snum
    print("Mul is",d)
except ValueError:
    print("Invalid Input...")
except ZeroDivisionError:
    print("Cannot Divide By Zero...")
except BaseException:
    print("Some Error...")
finally:
    print("It will always execute...")
