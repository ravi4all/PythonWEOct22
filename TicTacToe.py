import random

positions = [i for i in range(1,10)]
occupied = []

win_combinations = [
    [1,2,3], [4,5,6], [7,8,9],
    [1,4,7], [2,5,8], [3,6,9],
    [1,5,9], [3,5,7]
]

def gameBoard():
    print("""
        {} | {} | {}
        ------------
        {} | {} | {}
        ------------
        {} | {} | {}
    """.format(positions[0], positions[1], positions[2],
               positions[3], positions[4], positions[5],
               positions[6], positions[7], positions[8]))

def userMove(ch):
    pos = int(input("Enter your position : "))
    positions[pos - 1] = ch
    occupied.append(pos)

def cpuMove(ch):
    # CPU will choose a random number b/w 1 to 9
    # But that number should not be taken
    num = random.randint(1,9)
    if num in occupied:
        cpuMove(ch)
    else:
        print("CPU Moved at :",num)
        positions[num - 1] = ch
        occupied.append(num)

def main():
    gameBoard()
    user_ch = input("Enter your choice : 0/X : ")
    if user_ch == "0":
        cpu = "X"
    else:
        cpu = "0"

    while True:
        userMove(user_ch)
        gameBoard()
        cpuMove(cpu)
        gameBoard()

main()