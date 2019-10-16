class Board():

    board = list(("-") for x in range(9))

    def __init__(self, ox):
        self.ox = ox.upper()

    def update_board(self, pos, ox):
        self.board.pop(pos)
        self.board.insert(pos, ox)
        return self.board

    def player(self, pos):
        """Returns a new board in list format after players move"""
        if self.board[pos-1] == "-":
            x = self.board.pop(pos-1)
            self.board.insert(pos-1, self.ox)
        return self.board

    def check_h(self, player):
        """Check HORIZONTALLY whether win row is available"""
        first  = all((player == x for x in self.board[0:3])) #1,2,3
        second = all((player == x for x in self.board[3:6])) #4,5,6
        third = all((player == x for x in self.board[6:9]))  #7,8,9
        return any([first, second, third])

    def check_v(self, player):
        """Check VERTICALLY whether win row is available"""
        first  = all((player == x for x in self.board[0:7:3])) #1,4,7
        second = all((player == x for x in self.board[1:8:3])) #2,5,8
        third = all((player == x for x in self.board[2:9:3]))  #3,6,9
        return any([first, second, third])


    def check_diag_r(self, player):
        """Check whether in RIGHT DIAGONAL win row is available"""
        return all((player == self.board[x] for x in [0, 4, 8])) # 1, 5, 9

    def check_diag_l(self,player):
        """Check whether in LEFT DIAGONAL win row is available"""
        return all((player == self.board[x] for x in [2, 4, 6])) # 3, 5, 7

    def show(self):
        """CLI 3x3 visual output"""
        print("\n")
        for idx, i in enumerate(self.board, start=1):
            print("   " + i , end="  ")
            if idx % 3 == 0 and idx != 9:
                print(" ")
                print("...................")
        print(2*"\n")

    def answer_to_move(self, move, player):
        return self.board.insert(move, player)

    def __str__(self):
        """API format output of state"""
        return "".join(self.board)
