'''
a
ab
abc
abcd
abcde
'''
for i in range(5):
    for j in range(i+1):
        print(chr(97+j), end='')
    print()

print("=" * 30)

'''
a
b c
d e f
g h i j
k l m n o
'''
k = 64
for i in range(5):
    for j in range(i+1):
        k += 1
        print(chr(k)+" ", end='')
    print()






