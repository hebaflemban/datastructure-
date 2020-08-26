import numpy as np

maze_size = int(input("Enter the maze size: "))

maze = np.random.choice([0, 1], size=(maze_size, maze_size))

maze[0][0] = 0
maze[maze_size-1][maze_size-1] =  0

print(f"\n\n ***** MAZA ***** \n\n {maze} \n")

zeros = np.argwhere(maze == 0)
zeros = zeros.tolist()

start = zeros[0]
end = zeros[-1]

def get_out(zeros, start, end, path=[]):
    current = start
    path = path + [current]
    i = current[0]
    j = current[1]

    adjacents = [ [i+1, j+1],[i,j+1], [i+1,j] ]

    if current == end:
        return path

    for position in adjacents:
        if position in zeros:
            current = get_out(zeros, position, end, path)
            if current:
                return current
        else:
            pass

ones = get_out(zeros, start, end)

if ones:
    for i in range(len(ones)):
        x = ones[i]
        maze[x[0]][x[1]] = "8"

    print("WE GOT OUT!\n", maze)
else:
    print("There's no way out!")
