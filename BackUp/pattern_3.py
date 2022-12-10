'''
10101
10101
10101
10101
'''
for i in range(5):
    for j in range(5):
        if j % 2 != 0:
            print('0', end='')
        else:
            print('1', end='')
    print()

print("=" * 40)
