positions = [i for i in range(1,10)]

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

def cpuMove(ch):
    # CPU will choose a random number b/w 1 to 9
    # But that number should not be taken
    pass

def main():
    gameBoard()
    user_ch = input("Enter your choice : 0/X : ")
    if user_ch == "0":
        cpu = "X"
    else:
        cpu = "0"

    userMove(user_ch)
    gameBoard()
    cpuMove(cpu)

main()