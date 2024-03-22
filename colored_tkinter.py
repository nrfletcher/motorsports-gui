import tkinter as tk
from random import choice
import time

# Create the main window
root = tk.Tk()
root.title("Colored Squares")
root.minsize(1500, 800)

# Create a list of colors
colors = ['red', 'green', 'yellow']

# Create a list to store the square labels
squares = []

# Function to create a square label
def create_square(row, col):
    color = choice(colors)  # Randomly choose a color
    square = tk.Label(root, bg=color, width=10, height=5, relief='raised')
    square.grid(row=row, column=col)
    squares.append(square)

# Function to update the colors
def update_colors():
    for square in squares:
        square.config(bg=choice(colors))
    root.after(1000, update_colors)  # Call update_colors() after 1000 milliseconds (1 second)

# Create the 8x8 grid of squares
for row in range(8):
    for col in range(8):
        create_square(row, col)

# Start the color update loop
update_colors()

# Start the main event loop
root.mainloop()