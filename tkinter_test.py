import tkinter as tk
from random import choice

# Create the main window
root = tk.Tk()
root.title("Colored Squares")

# Create a list of colors
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown']

# Create a list to store the square labels
squares = []

# Function to create a square label
def create_square(row, col):
    color = choice(colors)  # Randomly choose a color
    square = tk.Label(root, bg=color, width=5, height=2, relief='raised')
    square.grid(row=row, column=col)
    squares.append(square)

# Create the 8x8 grid of squares
for row in range(8):
    for col in range(8):
        create_square(row, col)

# Start the main event loop
root.mainloop()