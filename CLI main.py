import requests
from Board import Board

def request_move(move, player):
    url = f"https://stujo-tic-tac-toe-stujo-v1.p.rapidapi.com/{move}/{player}"
    headers = {
    'x-rapidapi-host': "stujo-tic-tac-toe-stujo-v1.p.rapidapi.com",
    'x-rapidapi-key': "3efad19192msh6a98b6713edaf48p177302jsn3793168952fd"
    }

    response = requests.request("GET", url, headers=headers)
    return response.json()

def main():
    local_player =""
    print("W E L C O M E  T O  T H E  G A M E")
    print("==================================")
    print("            TIC TAC TOE           ")
    print(" by Stefan                  2019  ")
    print()

    while local_player not in ['x', 'X','o','O']:
        local_player = input('Chooose X or O : ').upper()
    if local_player == "X":
        api_player = "O"
    else:
        api_player = "X"
    board = Board(local_player)

    print()
    print("This is the playing board:")
    board.show()
    board.restart()
    while True:
        p_move = int(input('Chooose position [1-9]: '))
        while p_move in board.moves_made:
            print("\nAlready used! Choose different!")
            print(f"Your options {[x for x in range(1,10) if x not in board.moves_made]}\n")
            p_move = int(input('Chooose position [1-9]: '))

        if str(p_move) in '123456789':
            print()
            board.player(p_move)
            board.made_moves(p_move)
            print(f"Moves made: {board.moves_made}")
            board.show()
            win = board.check(board, local_player)
            if win:
                print("     C O N G R A T U L A T I O N S  !!!")
                print("--------------------------------------------")
                print(f'       YOU WON in {win[0]} LINE.')
                print()
                print('          G A M E  O V E R  !!!        ')
                break

            elif '-' not in board.board:
                print("        N O  W I N N E R  ! ! !     ")
                print("---------------------------------------\n")
                print("        G A M E  O V E R  ! ! !     ")
                break

            X = request_move(board, local_player)
            board.update_board(X['recommendation'], api_player)
            board.made_moves(X['recommendation']+1)
            print(f"Moves made: {board.moves_made}")
            print(f"Strenght of opponents move is [{X['strength']}]")
            board.show()

            lost = board.check(board, api_player)
            if lost:
                print("   W H A T  A  S H A M E  !!!")
                print("--------------------------------")
                print('   You lost against the API.')
                print(f'Your opponent won with {lost[0]} LINE.\n')
                print('     G A M E  O V E R  !!!        ')
                break
            elif '-' not in board.board:
                print("        N O  W I N N E R  ! ! !     ")
                print("---------------------------------------\n")
                print("        G A M E  O V E R  ! ! !     ")
                break

if __name__ == '__main__':
    play_gain = True
    while play_gain:
        main()
        play_gain = input("\nPlay again? [Y, N] : ").upper()
        if play_gain == 'N':
            play_gain = False
