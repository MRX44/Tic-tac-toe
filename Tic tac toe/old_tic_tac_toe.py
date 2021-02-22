P = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
S = "OX"

def show():
    print("╔═══╦═══╦═══╗")
    print("║ %s ║ %s ║ %s ║"%(P[0], P[1], P[2]))
    print("╠═══╬═══╬═══╣")
    print("║ %s ║ %s ║ %s ║"%(P[3], P[4], P[5]))
    print("╠═══╬═══╬═══╣")
    print("║ %s ║ %s ║ %s ║"%(P[6], P[7], P[8]))
    print("╚═══╩═══╩═══╝")

def replace(pos, xo):
    if P[pos] not in S:
        P[pos] = xo; return True
    else: return False

def check():
    if P[0] == P[1] == P[2] or P[3] == P[4] == P[5] or P[6] == P[7] == P[8] or\
       P[0] == P[3] == P[6] or P[1] == P[4] == P[7] or P[2] == P[5] == P[8] or\
       P[0] == P[4] == P[8] or P[6] == P[4] == P[2]: return True
    else: False

show()
C = 0
while C < 9:
    while not replace(int(input("Enter a place: ")) -1, S[C%2]): print("Error!!!")
    show()
    if check():
        print("%s wins"%(C%2))
        break
    C += 1
