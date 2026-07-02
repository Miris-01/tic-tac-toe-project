import numpy as np

def create_board():

    board = np.array([[' ', ' ', ' '], 
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']])
    return board


def display_board(board):
    #si es solamente para imprimir, podemos usar row
    for row in board:
        print(row)

def update_board(coord: tuple[int, int], simbol, board):
    #separamos los valores de las coordenadas en filas y columnas
    fila, columna = coord

    board[fila][columna] = simbol
    display_board(board)

    return board


def check_win(board, simbol):

    diag_win_1 = ((board.diagonal()) == simbol).all( )
    diag_win_2 = ((np.fliplr(board).diagonal()) == simbol).all()
    row_win = (board == simbol).all(axis=1).any()
    column_win = (board == simbol).all(axis=0).any()

    if diag_win_1 or diag_win_2 or row_win or column_win: 
        print(f'El jugador {simbol} gana la partida!!!')
        return True
    return False