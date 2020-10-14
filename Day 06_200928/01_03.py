from tkinter import *

c_height = 200
c_width = 300
c_colour = "black"

window = Tk()  # 하나의 화면 생성
window.title("MyCanvas")

# create_line
pen_x = c_width / 2  # 그림 그리는 시작 위치 - 가로의 정중앙
pen_y = c_height / 2  # 그림 그리는 시작 위치 - 세로의 정중앙

c = Canvas(bg=c_colour, height=c_height, width=c_width)
c.pack()


def pen_move_up(event):
    global pen_y
    # create_line(x_시작, y_시작, x_끝, y_끝, 선 굵기, 선 색깔)
    c.create_line(pen_x, pen_y, pen_x, pen_y - 5, width=5, fill='red')
    pen_y = pen_y - 5


def pen_move_down(event):
    global pen_y
    # create_line(x_시작, y_시작, x_끝, y_끝, 선 굵기, 선 색깔)
    c.create_line(pen_x, pen_y, pen_x, pen_y + 5, width=5, fill='blue')
    pen_y = pen_y + 5


def pen_move_left(event):
    global pen_x
    # create_line(x_시작, y_시작, x_끝, y_끝, 선 굵기, 선 색깔)
    c.create_line(pen_x, pen_y, pen_x - 5, pen_y, width=5, fill='yellow')
    pen_x = pen_x - 5


def pen_move_right(event):
    global pen_x
    # create_line(x_시작, y_시작, x_끝, y_끝, 선 굵기, 선 색깔)
    c.create_line(pen_x, pen_y, pen_x + 5, pen_y, width=5, fill='lightgreen')
    pen_x = pen_x + 5


window.bind("<Up>", pen_move_up)
window.bind("<Down>", pen_move_down)
window.bind("<Left>", pen_move_left)
window.bind("<Right>", pen_move_right)

window.mainloop()
