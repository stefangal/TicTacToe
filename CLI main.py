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

    PLAYER =""
    print("W E L C O M E  T O  T H E  G A M E")
    print("==================================")
    print("            TIC TAC TOE           ")
    print(" by Stefan                  2019  ")
    print()

    while PLAYER not in ['x', 'X','o','O']:
        PLAYER = input('Chooose X or O : ').upper()
    if PLAYER == "X":
        api_player = "O"
    else:
        api_player = "X"
    board = Board(PLAYER)

    print()
    print("This is the playing board:")
    board.show()
    while True:
        p_move = int(input('Chooose position [1-9]: '))
        if str(p_move) in '123456789':
            print()
            board.player(p_move)
            board.show()
            win = board.check(board, PLAYER)
            if win:
                print("     C O N G R A T U L A T I O N S  !!!")
                print("--------------------------------------------")
                print(f'       YOU WON in {win[0]} LINE.')
                print()
                print('          G A M E  O V E R  !!!        ')
                break
            elif '-' not in board.board:
                print("        N O  W I N N E R  ! ! !     ")
                print("----------------------------------------")
                print()
                print('     G A M E  O V E R  !!!        ')
                break

            X = request_move(board, PLAYER)
            board.update_board(X['recommendation'], api_player)
            print(f"Strenght of opponents move is [{X['strength']}]")
            board.show()

            lost = board.check(board, api_player)
            if lost:
                print("   W H A T  A  S H A M E  !!!")
                print("--------------------------------")
                print('You lost against the API.')
                print(f'API won with {lost[0]} LINE.')
                print()
                print('     G A M E  O V E R  !!!        ')
                break
            elif '-' not in board.board:
                print("        N O  W I N N E R  ! ! !     ")
                print("----------------------------------------")
                print()
                print('     G A M E  O V E R  !!!        ')
                break


if __name__ == '__main__':
    main()