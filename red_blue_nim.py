import sys

def pos_moves(state):
    moves = []
    if state[0] == 0:
        moves.append((0,state[1]-1))
    if state[1] == 0:
        moves.append((state[0]-1,0))
    elif state[0] > 0 and state[1] > 0:
        moves.append((state[0]-1,state[1]))
        moves.append((state[0],state[1]-1))
    return moves

def mm_alpbet(move, maxim, alpha,beta):
    if (move[0] == 0 or move[1] == 0) and not maxim:
        return (move[0]*2+move[1]*3)
    if (move[0] == 0 or move[1] == 0) and maxim:
        return -(move[0]*2+move[1]*3)
    if maxim:
        bscore = float("-inf")
        for moves in pos_moves(move):
            v = mm_alpbet(moves, False, alpha, beta)
            bscore = max(bscore, v)
            alpha  = max(alpha, bscore)
            if alpha >= beta :
                break
        return bscore

    else:
        bscore = float("inf")
        for moves in pos_moves(move):
            v = mm_alpbet(moves, True, alpha, beta)
            bscore = min(bscore, v)
            beta = min(beta, bscore)
            if alpha >= beta:
                break
        return bscore

def mm_alpbet_d(move, maxim, alpha,beta, depth):
    if (move[0] == 0 or move[1] == 0 or depth == 0) and maxim:
        msum = move[0]+move[1]
        if msum % 2 == 1:
            return (move[0]*2+move[1]*3)
        else:
            return -(move[0]*2+move[1]*3)
    if (move[0] == 0 or move[1] == 0 or depth == 0) and maxim == False:
        msum = move[0]+move[1]
        if msum % 2 == 1:
            return -(move[0]*2+move[1]*3)
        else:
            return (move[0]*2+move[1]*3)
    if maxim:
        bscore = float("-inf")
        for moves in pos_moves(move):
            v = mm_alpbet(moves, False, alpha, beta)
            bscore = max(bscore, v)
            alpha  = max(alpha, bscore)
            if alpha >= beta :
                break
        return bscore

    else:
        bscore = float("inf")
        for moves in pos_moves(move):
            v = mm_alpbet(moves, True, alpha, beta)
            bscore = min(bscore, v)
            beta = min(beta, bscore)
            if alpha >= beta:
                break
        return bscore


class state:
    def __init__(self, n_red, n_blue, player, tc, d):
        self.n_red = n_red
        self.n_blue = n_blue
        self.player = player
        self.tc = tc
        self.d = d

    def hmove(self, state):
        stack = None
        stack = input("human choose a color :")
        if stack == "red":
            self.n_red -= 1
            print("Move", self.tc, " - human choose: " ,stack)
            self.tc += 1
            self.player = 1 - self.player
        elif stack == "blue":
            self.n_blue -= 1
            print("Move", self.tc, " - human choose: " ,stack)
            self.tc += 1
            self.player = 1 - self.player
        else:
            print("invalid input")
            self.hmove(state)

    
    def cmove(self, state): 
        min, max = float("-inf"), float("inf")
        stack = None
        bestscore = float("-inf")
        for move in pos_moves([self.n_red, self.n_blue]):
            if self.d == None:
                nodescore = mm_alpbet(move, True, min, max)
            else:
                nodescore = mm_alpbet_d(move, True, min, max, self.d)
            if nodescore>bestscore:
                bestscore = nodescore
                choose = move

        if ((self.n_red),(self.n_blue-1))== choose:
            stack="blue"
        elif ((self.n_red-1, (self.n_blue)))== choose:
            stack="red"
        
        if stack == "red":
            self.n_red -= 1
        elif stack == "blue":
            self.n_blue -= 1
        
        print("Move", self.tc, " - Computer choose: " ,stack)
        self.tc += 1
        self.player = 1 - self.player
    

def nim(n_red, n_blue, ipl, d):
    if ipl == "computer":
        gstate = state(n_red, n_blue, 0, 1, d)
    elif ipl =="human":
        gstate = state(n_red, n_blue, 1, 1, d)

    while (gstate.n_red != 0 and gstate.n_blue != 0):
        print("red remaining: ", gstate.n_red, "blue remaining: ", gstate.n_blue)
        if gstate.player == 0:
            gstate.cmove(gstate)
        elif gstate.player == 1:
            gstate.hmove(gstate)

    if gstate.player == 0:
        print("red remaining: ", gstate.n_red, "blue remaining: ", gstate.n_blue)
        print("computer wins and computer scored: ", gstate.n_red*2+gstate.n_blue*3)
    elif gstate.player == 1:
        print("red remaining: ", gstate.n_red, "blue remaining: ", gstate.n_blue)
        print("Human wins and Human scored: ", gstate.n_red*2+gstate.n_blue*3)

if len(sys.argv) < 3:
    print("invalid input")
if len(sys.argv) == 5:
    n_red = int(sys.argv[1])
    n_blue = int(sys.argv[2])
    ipl = sys.argv[3]
    if ipl == "computer" or ipl == "human":
        pass
    else:
        ipl = input("who is intial player: ")
    d = int(sys.argv[4])
    nim(n_red, n_blue, ipl, d)
elif len(sys.argv)==4:
    n_red = int(sys.argv[1])
    n_blue = int(sys.argv[2])
    if len(sys.argv) < 5 or sys.argv[3] == "computer":
        ipl = "computer"  
    if sys.argv[3] == "human":
        ipl = "human"
    if sys.argv[3] !="computer" and sys.argv[3] != "human" and sys.argv[3].isnumeric() == False:
        print("You will have to start again")
        exit()
    d = int(sys.argv[3]) if (len(sys.argv) < 4 and (sys.argv[3]!="computer" or "human"))  else None
    nim(n_red, n_blue, ipl, d)
elif len(sys.argv)==3:
    n_red = int(sys.argv[1])
    n_blue = int(sys.argv[2])
    ipl = "computer"
    d = None
    nim(n_red, n_blue, ipl, d)