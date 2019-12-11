import turtle as trtl
import random
shape = "arrow"
maze_drawer = trtl.Turtle(shape = shape)
maze_drawer.speed(0)
maze_drawer.ht()
maze_drawer.pensize(5)

num_walls = 40
barrier_size = 30

wall_size = 10
wall_spacing = 15
door_width = 20

maze_drawer.backward(wall_size/2)
count = 0
barrier_skip = 0
def drawbarrier():
    global barrier_skip
    barrier_or_not = random.randint(1,2)
    if barrier_or_not <= 1:
        maze_drawer.right(90)
        maze_drawer.forward(barrier_size)
        maze_drawer.backward(barrier_size)
        maze_drawer.left(90)
    else:
        barrier_skip += 1

def drawdoor():
    maze_drawer.penup()
    maze_drawer.forward(door_width)
    maze_drawer.pendown()

while count < num_walls:
    if count > 3:

        door_loc = random.randint(door_width, wall_size-door_width*2)
        barrier_loc = random.randint(wall_spacing*2, wall_size-door_width*2)

        if door_loc < barrier_loc:
            maze_drawer.forward(door_loc)
            drawdoor()
            maze_drawer.forward(barrier_loc - door_loc - door_width)
            drawbarrier()
            maze_drawer.forward(wall_size - barrier_loc)
        else:
            maze_drawer.forward(barrier_loc)
            drawbarrier()
            maze_drawer.forward(door_loc - barrier_loc)
            drawdoor()
            maze_drawer.forward(wall_size - door_loc - door_width)
        maze_drawer.left(90)
    wall_size += wall_spacing
    count +=1


wn = trtl.Screen()
wn.mainloop()