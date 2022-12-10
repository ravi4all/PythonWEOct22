'''
*****
*   *
*   *
*   *
*****
'''
row = 5
col = 5
for i in range(row):
    for j in range(col):
        # first row, first col, last row, last col
        if i == 0 or j == 0 or i == row - 1 or j == col-1:
            print('*', end='')
        else:
            print(" ", end='')
    print()

print("=" * 40)

'''
*****
*   *
* * *
*   *
*****
'''
row = 5
col = 5
for i in range(row):
    for j in range(col):
        # first row, first col, last row, last col
        if i == 0 or j == 0 or i == row - 1 or j == col-1 or (i == row//2 and j == col//2):
            print('*', end='')
        else:
            print(" ", end='')
    print()

print("=" * 40)










