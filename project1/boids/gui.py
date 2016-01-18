from tkinter import *


def main():
    root = Tk()
    root.title = "IT3708 Project 1: Boids"

    frame = Frame(root)
    frame.pack()

    bottomframe = Frame(root)
    bottomframe.pack(side=BOTTOM)

    red_button = Button(frame, text="Red", fg="red")
    red_button.pack(side=LEFT)

    green_button = Button(frame, text="Green", fg="green")
    green_button.pack(side=LEFT)

    blue_button = Button(frame, text="Blue", fg="blue")
    blue_button.pack(side=LEFT)

    black_button = Button(bottomframe, text="Black", fg="black")
    black_button.pack(side=BOTTOM)

    root.mainloop()

if __name__ == '__main__':
    main()

