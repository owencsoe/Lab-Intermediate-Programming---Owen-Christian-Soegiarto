import tkinter as tk
from tkinter import messagebox, simpledialog

class TicTacToe:
    def _init_(self, root, size, win_length):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)
        self.size = size
        self.win_length = win_length
        self.current_player = "X"
        self.board = [""] * (size * size)
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()
        for i in range(self.size * self.size):
            button = tk.Button(frame, text="", font="Arial 20", width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i // self.size, column=i % self.size)
            self.buttons.append(button)
        self.reset_button = tk.Button(self.root, text="Restart", command=self.reset_game)
        self.reset_button.pack(pady=10)

    def on_button_click(self, index):
        if not self.board[index]:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.disable_buttons()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i * self.size + j] == self.current_player:
                    if self.check_direction(i, j, 1, 0) or \
                       self.check_direction(i, j, 0, 1) or \
                       self.check_direction(i, j, 1, 1) or \
                       self.check_direction(i, j, 1, -1):
                        return True
        return False

    def check_direction(self, row, col, delta_row, delta_col):
        count = 0
        for k in range(self.win_length):
            r = row + k * delta_row
            c = col + k * delta_col
            if 0 <= r < self.size and 0 <= c < self.size and self.board[r * self.size + c] == self.current_player:
                count += 1
            else:
                break
        return count == self.win_length

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state="disabled")

    def reset_game(self):
        self.board = [""] * (self.size * self.size)
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="", state="normal")

if __name__ == "_main_":
    root = tk.Tk()

    # Ask the user for the size of the board and the win length
    size = simpledialog.askinteger("Enter the size of the board (e.g., 3 for 3x3):", "Enter the size of the board (e.g., 3 for 3x3):", minvalue=3, maxvalue=10)
    if size:
        win_length = simpledialog.askinteger("Enter the win length (e.g., 3 for 3 in a row, max {size}", f"Enter the win length (e.g., 3 for 3 in a row, max {size}):", minvalue=3, maxvalue=size)
        if win_length:
            game = TicTacToe(root, size, win_length)
            root.mainloop()
