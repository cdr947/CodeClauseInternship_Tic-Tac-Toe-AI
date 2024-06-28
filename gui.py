import tkinter as tk
from tkinter import messagebox
import settings


class TicTacToe:
    def __init__(self, root):
        
        self.root = root
        self.root.overrideredirect(True)
        self.root.title("Tic Tac Toe")
        
        self.player = "X"
        self.ai = "O"
        self.board = [" " for _ in range(settings.BOARD_SIZE * settings.BOARD_SIZE)]
        self.buttons = []
        
        
        self.create_initial_screen()
        
 

    def center_window(self):
    # get screen width and height
        self.root.update()
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())
        x_cordinate = int((self.root.winfo_screenwidth() / 2) - (self.root.winfo_width() / 2))
        y_cordinate = int((self.root.winfo_screenheight() / 2) - (self.root.winfo_height() / 2))
        self.root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    def create_initial_screen(self):
        self.initial_frame = tk.Frame(self.root,bg= settings.THEME_BLACK)
        
        self.initial_frame.pack()
        


        label = tk.Label(self.initial_frame, text="Choose your symbol:", bg=settings.THEME_BLACK, fg= settings.THEME_WHITE, font=(settings.FONT_FAMILY, settings.FONT_SIZE_MEDIUM, settings.FONT_WEIGHT))
        label.pack()

        x_button = tk.Button(self.initial_frame, text="X",bg=settings.THEME_BLACK, fg= settings.THEME_WHITE, font=(settings.FONT_FAMILY, settings.FONT_SIZE_MEDIUM, settings.FONT_WEIGHT), command=lambda: self.start_game("X"))
        x_button.pack(side=tk.LEFT, padx=50)

        o_button = tk.Button(self.initial_frame, text="O", bg=settings.THEME_BLACK, fg= settings.THEME_WHITE,  font=(settings.FONT_FAMILY, settings.FONT_SIZE_MEDIUM, settings.FONT_WEIGHT), command=lambda: self.start_game("O"))
        o_button.pack(side=tk.RIGHT, padx=50)

        

    def start_game(self, player_symbol):
        self.player = player_symbol
        self.ai = "O" if player_symbol == "X" else "X"
        self.initial_frame.destroy()
        self.create_buttons()
        

    def create_buttons(self):
        for i in range(settings.BOARD_SIZE * settings.BOARD_SIZE):
            button = tk.Button(self.root,
                                text=" ",
                                font=(settings.FONT_FAMILY, settings.FONT_SIZE_LARGE, settings.FONT_WEIGHT),
                                height=2, width=5,
                                bg=settings.THEME_BLACK, fg= settings.THEME_WHITE, 
                                command=lambda i=i: self.button_click(i))
            button.grid(row=i//settings.BOARD_SIZE, column=i%settings.BOARD_SIZE)
            self.buttons.append(button)

    def button_click(self, index):
        if self.board[index] == " " and self.player_turn():
            self.board[index] = self.player
            self.buttons[index].config(text=self.player)
            if self.check_winner(self.player):
                self.game_over(settings.WIN_MESSAGE.format(self.player))
            elif " " not in self.board:
                self.game_over(settings.TIE_MESSAGE)
            else:
                
                self.ai_move()

    def player_turn(self):
        return self.player == "X" if self.player == "X" else self.player == "O"

    def ai_move(self):
        best_score = -float('inf')
        best_move = None
        for i in range(settings.BOARD_SIZE * settings.BOARD_SIZE):
            if self.board[i] == " ":
                self.board[i] = self.ai
                score = self.minimax(self.board, 0, False)
                self.board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i
        self.board[best_move] = self.ai
        self.buttons[best_move].config(text=self.ai)
        if self.check_winner(self.ai):
            self.game_over(settings.WIN_MESSAGE.format(self.ai))
        elif " " not in self.board:
            self.game_over(settings.TIE_MESSAGE)
        

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner(self.ai):
            return 1
        elif self.check_winner(self.player):
            return -1
        elif " " not in board:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(settings.BOARD_SIZE * settings.BOARD_SIZE):
                if board[i] == " ":
                    board[i] = self.ai
                    score = self.minimax(board, depth + 1, False)
                    board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(settings.BOARD_SIZE * settings.BOARD_SIZE):
                if board[i] == " ":
                    board[i] = self.player
                    score = self.minimax(board, depth + 1, True)
                    board[i] = " "
                    best_score = min(score, best_score)
            return best_score

    def check_winner(self, player):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] == player:
                return True
        return False

    def game_over(self, message):
        if messagebox.askyesno(settings.GAME_OVER_TITLE, settings.RESTART_PROMPT.format(message)):
            self.reset_game()
        else:
            self.root.destroy()

    def reset_game(self):
        self.board = [" " for _ in range(settings.BOARD_SIZE * settings.BOARD_SIZE)]
        for button in self.buttons:
            button.config(text=" ")
        self.create_initial_screen()

    