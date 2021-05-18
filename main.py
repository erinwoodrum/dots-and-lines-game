# after variables lesson

# Constants
size_of_board = 600
number_of_dots = 6
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
dot_color = '#7BC043'
player1_color = '#0492CF'
player1_color_light = '#67B0CF'
player2_color = '#EE4035'
player2_color_light = '#EE7E77'
Green_color = '#7BC043'
distance_between_dots = size_of_board / number_of_dots 
dot_width = .25 * distance_between_dots
edge_width = .1 * distance_between_dots

# Functions
def playerClick(event):
  print("click occurred!")

def drawBoard(c):
  for i in range(number_of_dots): 
    x = i * distance_between_dots+distance_between_dots/2
    
    c.create_line(x, distance_between_dots/2, x, size_of_board - distance_between_dots/2, fill='gray', dash = (2,2))

    c.create_line(distance_between_dots/2, x, size_of_board - distance_between_dots/2, x, fill='gray', dash=(2,2))
  
def drawDots(c):
  for i in range(number_of_dots):
    for j in range(number_of_dots): 
      start_x = i * distance_between_dots + distance_between_dots/2
      end_x = j * distance_between_dots + distance_between_dots/2

      c.create_oval(start_x - dot_width/2, end_x - dot_width/2, start_x + dot_width/2, end_x + dot_width/2, fill=dot_color, outline=dot_color)


# Create the board
from tkinter import *
window = Tk()
window.title("Dots and Line Game")
canvas = Canvas(window, width=size_of_board, height=size_of_board)
canvas.pack()
# Listen for user clicks
window.bind('<Button-1>', playerClick)
window.mainloop(30)
drawBoard(canvas)
drawDots(canvas)



# after tk intro



