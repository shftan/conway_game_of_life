import numpy as np

#// Use matplotlib for visualization
#// build grid
#// random cells shown alive
#// step 
#    // observe current state, determine new state for each cell
#    // plot the new state



# list of alive cells
# [(x1, y1), (x2, y2)]


# Function that given a cell, finds all of its neighbors
GRID_LENGTH = 10
GRID_WIDTH = 10

def check_boundaries(a):
    if a < 0 or a > 9:
        return False
    else:
        return True    

def find_alive_neighbors(grid, i, j):
    sum_alive_neighbours = 0
    sum_alive_neighbours += grid[i + 1, j + 1] if (check_boundaries(i + 1) and check_boundaries( j + 1)) else 0
    sum_alive_neighbours += grid[i + 1, j - 1] if (check_boundaries(i + 1) and check_boundaries( j - 1)) else 0
    sum_alive_neighbours += grid[i - 1, j - 1] if (check_boundaries(i - 1) and check_boundaries( j - 1)) else 0
    sum_alive_neighbours += grid[i - 1, j + 1] if (check_boundaries(i - 1) and check_boundaries( j + 1)) else 0
    sum_alive_neighbours += grid[i - 1, j] if (check_boundaries(i - 1) and check_boundaries( j)) else 0
    sum_alive_neighbours += grid[i + 1, j] if (check_boundaries(i + 1) and check_boundaries( j)) else 0
    sum_alive_neighbours += grid[i, j - 1] if (check_boundaries(i) and check_boundaries( j - 1)) else 0
    sum_alive_neighbours += grid[i, j + 1] if (check_boundaries(i) and check_boundaries( j + 1)) else 0
    return sum_alive_neighbours

def get_new_state(old_grid):
    new_grid = np.zeros((GRID_LENGTH, GRID_WIDTH))

    for i in range(GRID_LENGTH):
        for j in range(GRID_WIDTH):
            x = find_alive_neighbors(old_grid, i, j)

            if (old_grid[i, j] == 1 and x > 1 and x < 4):
                new_grid[i, j] = 1

            if (old_grid[i, j] == 0 and x == 3):
                new_grid[i, j] = 1

    return new_grid


# Function that initializes a grid given user input
# The grid will have values 0 or 1. 0 indicates dead, 1 indicates alive
def initialize_grid():
    grid = np.zeros((GRID_LENGTH, GRID_WIDTH))
    grid = np.random.randint(2, size=(GRID_LENGTH, GRID_WIDTH))
    return grid


if __name__ == "__main__":
    old_grid = initialize_grid()
    print(old_grid)
    for x in range(100):
        grid = get_new_state(old_grid)
        print(grid)
        old_grid = grid
