class Board():
    def __init__(self, ox):
        self.ox = ox.upper()

    board = list(("-") for x in range(9))
    moves_made = []


    def update_board(self, pos, ox):
        self.board.pop(pos)
        self.board.insert(pos, ox)
        return self.board

    def player(self, pos):
        """Returns a new board in list format after players move"""
        if pos not in self.moves_made:
            x = self.board.pop(pos-1)
            self.board.insert(pos-1, self.ox)
        return self.board

    def check(self, bd, player):
        bd = self.board
        first_h  = all((player == x for x in bd[0:3])) #1,2,3
        second_h = all((player == x for x in bd[3:6])) #4,5,6
        third_h = all((player == x for x in bd[6:9]))  #7,8,9
        first_v  = all((player == x for x in bd[0:7:3])) #1,4,7
        second_v = all((player == x for x in bd[1:8:3])) #2,5,8
        third_v = all((player == x for x in bd[2:9:3]))  #3,6,9

        if any([first_h, second_h, third_h]):
            return ['HORIZONTAL', player]
        elif any([first_v, second_v, third_v]):
            return ['VERTICAL', player]
        elif all((player == self.board[x] for x in [0, 4, 8])): # 1, 5, 9
            return ['RIGHT DIAGONAL', player]
        elif all((player == self.board[x] for x in [2, 4, 6])): # 3, 5, 7
            return ['LEFT DIAGONAL', player]
        return False

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

    @classmethod
    def made_moves(cls, pos):
        cls.moves_made.append(pos)

    def __str__(self):
        """API format output of state"""
        return "".join(self.board)

    def restart(self):
        self.moves_made = []
        self.board = list(("-") for x in range(9))