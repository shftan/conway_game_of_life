import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

GRID_LENGTH = 10
GRID_WIDTH = 10

# Functions to check if proposed cell coordinates are out-of-bounds
def check_boundaries_length(a):
    if a < 0 or a > (GRID_LENGTH-1):
        return False
    else:
        return True    
    
def check_boundaries_width(b):
    if b < 0 or b > (GRID_WIDTH-1):
        return False
    else:
        return True    

# Function that given a cell, finds all of its neighbors
def find_alive_neighbors(grid, i, j):
    sum_alive_neighbours = 0
    sum_alive_neighbours += grid[i + 1, j + 1] if (check_boundaries_length(i + 1) and check_boundaries_width(j + 1)) else 0
    sum_alive_neighbours += grid[i + 1, j - 1] if (check_boundaries_length(i + 1) and check_boundaries_width(j - 1)) else 0
    sum_alive_neighbours += grid[i - 1, j - 1] if (check_boundaries_length(i - 1) and check_boundaries_width(j - 1)) else 0
    sum_alive_neighbours += grid[i - 1, j + 1] if (check_boundaries_length(i - 1) and check_boundaries_width(j + 1)) else 0
    sum_alive_neighbours += grid[i - 1, j] if (check_boundaries_length(i - 1) and check_boundaries_width(j)) else 0
    sum_alive_neighbours += grid[i + 1, j] if (check_boundaries_length(i + 1) and check_boundaries_width(j)) else 0
    sum_alive_neighbours += grid[i, j - 1] if (check_boundaries_length(i) and check_boundaries_width(j - 1)) else 0
    sum_alive_neighbours += grid[i, j + 1] if (check_boundaries_length(i) and check_boundaries_width(j + 1)) else 0
    return sum_alive_neighbours

# Function that goes from the current grid to the new grid, applying the Game of Life rules 
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

# Function to plot a given grid
def plot_grid(frame, im, title_artist):
    grid, step_num = frame
    im.set_data(grid)
    title_artist.set_text(f"""Step: {step_num}""")
    return (im, title_artist)

def init():
    im.set_data(old_grid)
    title_artist.set_text("Step: 0")
    return (im, title_artist)

# Main function
if __name__ == "__main__":
    old_grid = initialize_grid()

    fig, ax = plt.subplots()
    im = ax.imshow(old_grid, cmap="binary", vmin=0, vmax=1, interpolation="nearest", animated=True)
    title_artist = ax.set_title("Step: 0")
    
    frames = []
    grid = old_grid
    for step in range(100):
        frames.append((grid, step))
        grid = get_new_state(grid)

    ani = FuncAnimation(
        fig,
        plot_grid,
        frames=frames,
        fargs=(im, title_artist),
        init_func=init,
        blit=False,
        interval=1000,
        repeat=False,
    )

    plt.show()