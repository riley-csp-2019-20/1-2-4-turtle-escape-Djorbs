import turtle as trtl
import random
shape = "arrow"
maze_drawer = trtl.Turtle(shape = shape)
maze_drawer.speed(0)
maze_drawer.ht()

count = 0
num_walls = 25
wall_spacing = 25
def random_barrier():
    rbarrier = random.randint(1,10)
def random_location():
    global total_wall
    rlocation = random.randit(1,total_wall)

def barrier():
    random_barrier()
    global rbarrier
    global rlocation
    if rbarrier <= 3:
        if count > 3:
            random_location()
            maze_drawer.backward(rlocation)



while count < num_walls:
    maze_drawer.left(90)
    wall_size = (25 + (count * wall_spacing))
    solid_wall = wall_size/2
    gap_wall = wall_spacing + 5
    maze_drawer.forward(solid_wall)
    maze_drawer.penup()
    maze_drawer.forward(gap_wall)
    maze_drawer.pendown()
    maze_drawer.forward(solid_wall)
    total_wall = solid_wall*2 + gap_wall
    barrier()
    count += 1

wn = trtl.Screen()
wn.mainloop()