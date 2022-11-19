'''
    *
   **
  ***
 ****
*****
'''
for i in range(5):
    for j in range(5-i):
        print(' ', end='')
    for j in range(i+1):
        print('*', end='')
    print()

print("=" * 30)

'''
    *
   * *
  * * *
 * * * *
* * * * *
'''
for i in range(5):
    for j in range(5-i):
        print(' ', end='')
    for j in range(i+1):
        print('* ', end='')
    print()


print("=" * 30)

'''
    *
   ***
  *****
 *******
*********
'''
for i in range(5):
    for j in range(5-i):
        print(' ', end='')
    for k in range(2*i+1):
        print('*', end='')
    print()

print("=" * 30)

'''
*********
 *******
  *****
   ***
    *
'''
for i in range(5,-1,-1):
    for j in range(5-i):
        print(' ', end='')
    for k in range(2*i+1):
        print('*', end='')
    print()




