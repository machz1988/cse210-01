# Assigment: CSE 210. W02 Prove: Developer - Solo Code Submission
# Author: Manuel Cipriano 
from textwrap import indent

class TicTacToeGame:
    def __init__(self):
        self.board = [['1','2','3'],['4','5','6'],['7','8','9']]
        self.player1 = True
        self.player2 = False
        self.chances = 9

    def play(self):
        self.print_board()
        while self.chances > 0:
            position = 0
            index = [-1, -1]
            
            if self.player1 == True:
                while position < 1 or position > 9: 
                    position = int(input("X's turn to choose a square (1-9) "))
                    index = self.index_conversion(position)
                    data = self.board[index[0]][index[1]]
                    if not data.isnumeric():
                        position = 0
                self.player1 = False
                self.player2 = True
                self.board[index[0]][index[1]] = "X"
            else:
                while position < 1 or position > 9: 
                    position = int(input("O's turn to choose a square (1-9) "))
                    index = self.index_conversion(position)
                    data = self.board[index[0]][index[1]]
                    if not data.isnumeric():
                        position = 0
                self.player1 = True
                self.player2 = False
                self.board[index[0]][index[1]] = "O"
            self.chances -= 1
            index = self.index_conversion(position)
            #print(f'{index[0]}, {index[1]}')
            self.print_board()
            if self.chances < 5:
                if self.check_status_game():
                    print("Good game. Thanks for playing!")
                    break

    def print_board(self):
        print(f'{self.board[0][0]}  |   {self.board[0][1]}  |   {self.board[0][2]}')
        print("---+------+----")
        print(f'{self.board[1][0]}  |   {self.board[1][1]}  |   {self.board[1][2]}')
        print("---+------+----")
        print(f'{self.board[2][0]}  |   {self.board[2][1]}  |   {self.board[2][2]}')

    def check_status_game(self):
        data = 'O'
        if self.board[0].count(data) == 3:
            return True
        elif self.board[1].count(data) == 3:
            return True
        elif self.board[2].count(data) == 3:
            return True

        data = 'X'
        if self.board[0].count(data) == 3:
            return True
        elif self.board[1].count(data) == 3:
            return True
        elif self.board[2].count(data) == 3:
            return True
        
        data = 'O'
        column1 = [self.board[0][0], self.board[1][0], self.board[2][0]]
        if column1.count(data) == 3:
            return True
        
        data = 'X'
        if column1.count(data) == 3:
            return True

        data = 'O'
        column2 = [self.board[0][1], self.board[1][1], self.board[2][1]]
        if column2.count(data) == 3:
            return True
        
        data = 'X'
        if column2.count(data) == 3:
            return True
    
        data = 'O'
        column3 = [self.board[0][2], self.board[1][2], self.board[2][2]]
        if column3.count(data) == 3:
            return True
        
        data = 'X'
        if column3.count(data) == 3:
            return True
        
        data = 'O'
        diagonal1 = [self.board[0][0], self.board[1][1], self.board[2][2]]
        if diagonal1.count(data) == 3:
            return True
        
        data = 'X'
        if diagonal1.count(data) == 3:
            return True

        data = 'O'
        diagonal2 = [self.board[0][2], self.board[1][1], self.board[2][0]]
        if diagonal2.count(data) == 3:
            return True
        
        data = 'X'
        if diagonal2.count(data) == 3:
            return True
        return False

    def index_conversion(self, relative_index):
        index = [0, 0]
        if relative_index > 0 and relative_index < 10:
            if relative_index == 2:
                index = [0, 1]
            elif relative_index == 3:
                index = [0, 2]
            elif relative_index == 4:
                index = [1, 0]
            elif relative_index == 5:
                index = [1, 1]
            elif relative_index == 6:
                index = [1, 2]
            elif relative_index == 7:
                index = [2, 0]
            elif relative_index == 8:
                index = [2, 1]
            elif relative_index == 9:
                index = [2, 2]
        else:
            index = [-1, -1]
        return index

def main():
    game = TicTacToeGame()
    game.play()

if __name__ == "__main__":
    main()