import tkinter as tk
from tkinter import messagebox
import random

class Puzzle15:
    def __init__(self, master, size):
        self.master = master
        self.master.title("Пятнашки")
        self.size = size
        self.tiles = []
        self.empty_row = size - 1
        self.empty_col = size - 1

        self.frame = tk.Frame(self.master)

    def create_game(self):
        self.frame.pack()
        numbers = list(range(1, self.size ** 2))
        random.shuffle(numbers)
        numbers.append("")
        self.tiles.clear()

        # Вычисляем размер клеток в пикселях
        button_width = int(50 / self.size)  # Общая ширина рамки - 200 пикселей
        button_height = int(25 / self.size)  # Общая высота рамки - 150 пикселей
        

        for i in range(self.size):
            for j in range(self.size):
                index = i * self.size + j
                tile = tk.Button(self.frame, text=numbers[index], width=button_width, height=button_height,
                                 command=lambda i=i, j=j: self.move(i, j))
                tile.grid(row=i, column=j)
                self.tiles.append(tile)

        self.empty_row = self.size - 1
        self.empty_col = self.size - 1

    def move(self, row, col):
        if self.is_adjacent(row, col):
            index = row * self.size + col
            empty_index = self.empty_row * self.size + self.empty_col
            self.tiles[empty_index]["text"] = self.tiles[index]["text"]
            self.tiles[index]["text"] = ""
            self.empty_row = row
            self.empty_col = col
            if self.check_win():
                messagebox.showinfo("Пятнашки", "Вы выиграли!")
            if self.tiles[index]["text"] == str(index + 1):
                self.tiles[index].configure(bg="lightgreen")
            else:
                self.tiles[index].configure(bg=self.master.cget("bg"))

    def is_adjacent(self, row, col):
        return (abs(row - self.empty_row) == 1 and col == self.empty_col) or \
               (row == self.empty_row and abs(col - self.empty_col) == 1)

    def check_win(self):
        for i, tile in enumerate(self.tiles[:-1]):
            if tile["text"] != str(i + 1):
                return False
        return True

def start_game():
    global puzzle
    if puzzle:
        puzzle.frame.destroy()  # Удаляем предыдущую игру с поля
    selected_size = int(size_var.get())
    puzzle = Puzzle15(root, selected_size)
    puzzle.create_game()

root = tk.Tk()
root.title("Выбор уровня")
root.geometry("200x150")

size_var = tk.StringVar(root)
size_var.set("3")

size_label = tk.Label(root, text="Выберите размер поля:")
size_label.pack(pady=5)

size_menu = tk.OptionMenu(root, size_var, "3", "4", "5", "6")
size_menu.pack(pady=5)

start_button = tk.Button(root, text="Начать игру", command=start_game)
start_button.pack(pady=10)

puzzle = None  # Глобальная переменная для текущей игры

root.mainloop()
