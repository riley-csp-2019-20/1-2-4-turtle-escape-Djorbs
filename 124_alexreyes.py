import turtle as trtl
shape = "arrow"
maze_drawer = trtl.Turtle(shape = shape)
maze_drawer.speed(0)
maze_drawer.ht()

count = 0
num_walls = 25
wall_spacing = 25

def barrier():
    if count > 3:
        maze_drawer.right(90)
        maze_drawer.forward(wall_spacing*1.95)
        maze_drawer.backward(wall_spacing*1.95)
        maze_drawer.left(90)

while count < num_walls:
    maze_drawer.left(90)
    wall_size = (25 + (count * wall_spacing))
    solid_wall = wall_size/2
    gap_wall = wall_spacing + 5
    maze_drawer.forward(solid_wall)
    maze_drawer.penup()
    maze_drawer.forward(gap_wall)
    maze_drawer.pendown()
    barrier()
    maze_drawer.forward(solid_wall)
    count += 1

wn = trtl.Screen()
wn.mainloop()