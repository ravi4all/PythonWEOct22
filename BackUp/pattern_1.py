#Pattern Programs

#*****
#print('*' * 5)

'''
*****
*****
*****
*****
*****
'''
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()

print("=" * 40)




'''
*
**
***
****
*****
'''
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()

print("=" * 40)


'''
1
12
123
1234
12345
'''
for i in range(5):
    for j in range(i+1):
        print(j+1, end='')
    print()

print("=" * 40)



'''
*****
****
***
**
*
'''
for i in range(5):
    for j in range(5-i):
        print('*', end='')
    print()

print("=" * 40)




'''
54321
5432
543
54
5
'''
for i in range(5):
    for j in range(5,i,-1):
        print(j, end='')
    print()

print("=" * 40)



'''
1
2 3
4 5 6
7 8 9 10
'''
k = 0
for i in range(5):
    for j in range(i+1):
        k += 1
        print(k," ", end='')
    print()

print("=" * 40)






