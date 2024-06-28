from gui import TicTacToe
import tkinter as tk




if __name__ == "__main__":
    root = tk.Tk()
    
    game = TicTacToe(root)
    game.center_window()


    
    root.mainloop()
