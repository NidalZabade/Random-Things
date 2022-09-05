
import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.resizable(0, 0)
        self.root.wm_attributes("-topmost", 1)
        self.frame = tk.Frame(self.root, width=300, height=300)
        self.frame.pack()
        self.canvas = tk.Canvas(self.frame, width=300, height=300, bd=0, highlightthickness=0)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.click)
        self.root.update()
        self.x = -1
        self.y = -1
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.player = 1
        self.draw_board()
        self.root.mainloop()

    def draw_board(self):
        self.canvas.delete("all")
        self.canvas.create_line(100, 0, 100, 300, width=2)
        self.canvas.create_line(200, 0, 200, 300, width=2)
        self.canvas.create_line(0, 100, 300, 100, width=2)
        self.canvas.create_line(0, 200, 300, 200, width=2)
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 1:
                    self.canvas.create_line(i * 100 + 15, j * 100 + 15, i * 100 + 85, j * 100 + 85, width=2)
                    self.canvas.create_line(i * 100 + 15, j * 100 + 85, i * 100 + 85, j * 100 + 15, width=2)
                elif self.board[i][j] == 2:
                    self.canvas.create_oval(i * 100 + 15, j * 100 + 15, i * 100 + 85, j * 100 + 85, width=2)

    def click(self, event):
        if self.player == 1:
            self.x = event.x // 100
            self.y = event.y // 100
            if self.board[self.x][self.y] == 0 and self.winner() == 0:
                self.board[self.x][self.y] = 1
                self.draw_board()
                self.player = 2
                self.ai()
                if self.winner() == 2:
                    messagebox.showinfo("Tic Tac Toe", "You lose!")
                    self.root.destroy()
                elif self.winner() == 1:
                    messagebox.showinfo("Tic Tac Toe", "You win!")
                    self.root.destroy()
                elif self.winner() == -1:
                    messagebox.showinfo("Tic Tac Toe", "Draw!")
                    self.root.destroy()

        
    def ai(self):
        if self.winner() == 0:
            move = self.minimax(self.board, 2)
            self.board[move[0]][move[1]] = 2
            self.draw_board()
            self.player = 1

    
    


    def minimax(self, board, player):
        winner = self.winner()
        if winner != 0:
            return [None, None, winner]
        elif player == 2:
            best = [-1, -1, -10]
        else:
            best = [-1, -1, 10]
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = player
                    score = self.minimax(board, 3 - player)
                    board[i][j] = 0
                    score[0] = i
                    score[1] = j
                    if player == 2:
                        if score[2] > best[2]:
                            best = score
                    else:
                        if score[2] < best[2]:
                            best = score
        return best
    
    def winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return self.board[0][0]
        if self.board[2][0] == self.board[1][1] == self.board[0][2] != 0:
            return self.board[2][0]
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return 0
        return -1
    
if __name__ == "__main__":
    game = TicTacToe()
