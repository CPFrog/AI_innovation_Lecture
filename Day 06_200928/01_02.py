from tkinter import *

c_height = 400
c_width = 600
c_colour = "black"

window = Tk()  # 하나의 화면 생성
window.title("MyCanvas")

c = Canvas(bg=c_colour, height=c_height, width=c_width)
c.pack()

label = Label(window, text="Hello World!")
label2 = Label(window, text='20200928')

label.pack()
label2.pack()

window.mainloop()
