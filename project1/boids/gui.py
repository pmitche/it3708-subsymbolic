from tkinter import *

HEIGHT = 600
WIDTH = 1000


def add_obstacle():
    pass


def remove_obstacles():
    pass


def add_predator():
    pass


def remove_predators():
    pass


def update_separation(value):
    print("Updating separation: {}".format(value))


def update_alignment(value):
    print("Updating alignment: {}".format(value))


def update_cohesion(value):
    print("Updating cohesion: {}".format(value))

def main():
    root = Tk()
    root.title = "IT3708 Project 1: Boids"

    canvas = Canvas(root, bg="black", height=HEIGHT, width=WIDTH)
    canvas.create_polygon([20, 10, 15, 25, 25, 25], fill="white")
    canvas.pack()


    bottomframe = Frame(root)
    bottomframe.pack(side=BOTTOM)

    ######################################################################################
    # OBSTACLES
    ######################################################################################

    obstacles_frame = Frame(bottomframe, bd=2, relief=RIDGE, padx=5, pady=10)
    obstacles_frame.pack(side=LEFT, padx=20)

    obstacles_label = Label(obstacles_frame, text="Obstacles", font=("Helvetica", 18), pady=10)
    obstacles_label.pack(side=TOP)

    add_obstacle_button = Button(obstacles_frame, text="Add random obstacle", pady=10, width=20, command=add_obstacle())
    add_obstacle_button.pack()

    remove_obstacles_button = Button(obstacles_frame, text="Remove all obstacles", pady=10, width=20, command=remove_obstacles())
    remove_obstacles_button.pack()

    ######################################################################################
    # PREDATORS
    ######################################################################################

    predators_frame = Frame(bottomframe, bd=2, relief=RIDGE, padx=5, pady=10)
    predators_frame.pack(side=LEFT, padx=20)

    predators_label = Label(predators_frame, text="Predators", font=("Helvetica", 18), pady=10)
    predators_label.pack(side=TOP)

    add_predator_button = Button(predators_frame, text="Add random predator", pady=10, width=20, command=add_predator())
    add_predator_button.pack()

    remove_predators_button = Button(predators_frame, text="Remove all predators", pady=10, width=20, command=remove_predators())
    remove_predators_button.pack()

    ######################################################################################
    # WEIGHTS
    ######################################################################################

    weights_frame = Frame(bottomframe, bd=2, relief=RIDGE, padx=5, pady=10)
    weights_frame.pack(side=LEFT)

    w_label = Label(weights_frame, text="Weights", font=("Helvetica", 18))
    w_label.pack(side=TOP, pady=10)

    separation_scale = Scale(weights_frame, length=140, label="Separation", orient=HORIZONTAL, command=update_separation)
    separation_scale.set(30)
    separation_scale.pack(side=LEFT, padx=10, pady=10)

    alignment_scale = Scale(weights_frame, length=140, label="Alignment", orient=HORIZONTAL, command=update_alignment)
    alignment_scale.set(50)
    alignment_scale.pack(side=LEFT, padx=10, pady=10)

    cohesion_scale = Scale(weights_frame, length=140, label="Cohesion", orient=HORIZONTAL, command=update_cohesion)
    cohesion_scale.set(65)
    cohesion_scale.pack(side=LEFT, padx=10, pady=10)

    root.mainloop()

if __name__ == '__main__':
    main()

