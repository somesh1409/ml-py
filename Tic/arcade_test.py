import arcade
import numpy

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "TIC TAC TOE"
BOARD_ROWS = 3
BOARD_COLS = 3


class TicTacToe(arcade.Window):
    def __init__(self, width, height, title, rows, columns):
        super().__init__(width, height, title)
        
        self.width = width
        self.height = height
        self.rows = rows
        self.columns = columns
        self.a = self.height/self.columns
        self.boardSprites = arcade.SpriteList() 
    
    def setup(self):
        colorBlack = False
        colorBlackInit = False
        a = self.a
        y = self.height/(2*self.columns)
        for i in range(self.rows):
            x = self.width/(2*self.rows)
            for j in range(self.columns):
                arcade.draw_rectangle_filled(x, y, a, a, arcade.color.GRAY_BLUE if colorBlack else arcade.color.ALICE_BLUE)
                colorBlack = not(colorBlack)
                x += a
            colorBlack = not(colorBlackInit)
            colorBlackInit = not(colorBlackInit)
            y += a

    def on_draw(self):
        arcade.start_render()
        self.setup()
        self.boardSprites.draw()

    def printBoard(self, board):
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                if board[i, j] == 1:
                    print("Cross")
                    cross = arcade.Sprite("images/cross.png", center_x=self.a*(i+0.5), center_y=self.a*(j+1/2), scale=0.18)
                    self.boardSprites.append(cross)
                elif board[i, j] == -1:
                    zero = arcade.Sprite("images/zero.png", center_x=self.a*(i+1/2), center_y=self.a*(j+1/2), scale=0.22)
                    self.boardSprites.append(zero)
        
# app = TicTacToe(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, BOARD_ROWS, BOARD_COLS)
# # app.setup()
# board = numpy.zeros((BOARD_ROWS, BOARD_COLS))
# board[1,1] = 1
# app.printBoard(board)
# arcade.run()
# print("Here!")