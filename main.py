###
# Write function on Python 3  function that will create a spiral with a given size.
#
#     For example, spiral with size 5 should look like this:
#
#     00000
#     ....0
#     000.0
#     0...0
#     00000
#     and with the size 10:
#
#     0000000000
#     .........0
#     00000000.0
#     0......0.0
#     0.0000.0.0
#     0.0..0.0.0
#     0.0....0.0
#     0.000000.0
#     0........0
#     0000000000
#
## Return value should contain array of arrays, of 0 and 1, with the first row being composed of 1s. For example for given size 5 result should be:
#
#     [[1,1,1,1,1],
#      [0,0,0,0,1],
#      [1,1,1,0,1],
#      [1,0,0,0,1],
#      [1,1,1,1,1]]
#
#     Because of the edge-cases for tiny spirals, the size will be at least 5.
#
#     General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.


import random

test_case = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]



def spiralize(size):
    # Create an empty maze
    maze = [[0 for _ in range(size)] for _ in range(size)]
    visited = set()

    # Choose a random starting cell and add it to the maze
    start_row = random.randint(0, size - 1)
    start_col = random.randint(0, size - 1)
    maze[start_row][start_col] = 1
    visited.add((start_row, start_col))

    # Recursive function to grow the maze
    def grow_maze(row, col):
        # Create a list of possible directions to grow
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)

        # Try to grow in each direction
        for d_row, d_col in directions:
            new_row, new_col = row + 2 * d_row, col + 2 * d_col
            if (new_row, new_col) not in visited and 0 <= new_row < size and 0 <= new_col < size:
                # Mark the new cell as part of the maze
                maze[new_row][new_col] = 1
                visited.add((new_row, new_col))
                # Mark the cell between the new cell and the current cell as part of the maze
                maze[row + d_row][col + d_col] = 1
                # Recursively grow the maze from the new cell
                grow_maze(new_row, new_col)

    # Start growing the maze from the starting cell
    grow_maze(start_row, start_col)

    return maze


def test_spiralize(spiralize):
    test_case = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                 [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
                 [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
                 [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                 [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                 [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    if test_case == spiralize:
        return True
    else:
        return False


for item in spiralize(5):
    print(item)

a = 1
b = 2

while a != b:
    print(">>>")
    c = spiralize(10)
    for item in c:
        print(item)

    b = True
    a = test_spiralize(spiralize)


print(">>> >>>")
for item in c:
    print(item)



