class PseudoBoard():

    board = list(("-") for x in range(9))

    def __init__(self, ox):
        self.ox = ox.upper()


    def player(self, pos):
        """Returns a new board in list format after players move"""
        if self.board[pos-1] == "-":
            x = self.board.pop(pos-1)
            self.board.insert(pos-1, self.ox)
        return self.board

    def checkH(self):
        """Check HORIZONTALLY whether win row is available"""
        first  = all((self.ox == x for x in self.board[0:3])) #1,2,3
        second = all((self.ox == x for x in self.board[3:6])) #4,5,6
        third = all((self.ox == x for x in self.board[6:9]))  #7,8,9
        return any([first, second, third])

    def checkV(self):
        """Check VERTICALLY whether win row is available"""
        first  = all((self.ox == x for x in self.board[0:7:3])) #1,4,7
        second = all((self.ox == x for x in self.board[1:8:3])) #2,5,8
        third = all((self.ox == x for x in self.board[2:9:3]))  #3,6,9
        return any([first, second, third])


    def checkDiagR(self):
        """Check whether in RIGHT DIAGONAL win row is available"""
        return all((self.ox == self.board[x] for x in [0, 4, 8])) # 1, 5, 9

    def checkDiagL(self):
        """Check whether in LEFT DIAGONAL win row is available"""
        return all((self.ox == self.board[x] for x in [2, 4, 6])) # 3, 5, 7

    def show(self):
        """CLI 3x3 visual output"""
        print("\n")
        for idx, i in enumerate(self.board, start=1):
            print("   " + i , end="  ")
            if idx % 3 == 0 and idx != 9:
                print(" ")
                print("...................")
        print(2*"\n")

    def __str__(self):
        """API format output of state"""
        return "".join(self.board)



board = PseudoBoard("X")
board.player(7)
board.player(8)
board.player(5)
print(f"Horizontal: {board.checkH()}")
print(f"Vertical:   {board.checkV()}")
print(f"Diagonal L: {board.checkDiagL()}")
print(f"Diagonal R: {board.checkDiagR()}")
board.show()



