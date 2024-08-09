import time

DEAD = '.'
ALIVE = '#'


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


################################
######## CLASS CELL MAP ########
################################
class CellMap:
    def __init__(self, file_name):
        self.cnt = 0
        self.cells_map = self.parse_file(file_name)

    # Used to display the map cause print() use str() method
    def __str__(self):
        return '\n'.join([''.join(line) for line in self.cells_map])

    def parse_file(self, file_name):
        cells = []
        with open(file_name, 'r') as file:
            for line in file:
                cells.append(list(line.strip()))
        return cells

    def count_alive_neighbours(self, row, col, nb_row, nb_col):
        cnt = 0
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if i == 0 and j == 0:
                    continue
                if 0 <= i + row < nb_row and 0 <= j + col < nb_col:
                    if self.cells_map[i + row][j + col] == ALIVE:
                        cnt += 1
        return cnt

    def update_cell(self, cell_state, nb_alive_neighbours):
        if cell_state == ALIVE:
            if nb_alive_neighbours < 2 or nb_alive_neighbours > 3:
                return DEAD
            return ALIVE
        if cell_state == DEAD:
            if nb_alive_neighbours == 3:
                return ALIVE
            return DEAD

    def update_grid(self, nb_row, nb_col):
        new_cells_map = []
        for i in range(nb_row):
            new_line = []
            for j in range(nb_col):
                alive_cell = self.count_alive_neighbours(i, j, nb_row, nb_col)
                new_line.append(
                    self.update_cell(self.cells_map[i][j], alive_cell))
            new_cells_map.append(new_line)
        return new_cells_map

    def run_iterations(self, num_iterations):
        print(self)
        print()
        for _ in range(num_iterations):
            nb_row = len(self.cells_map)
            nb_col = len(self.cells_map[0])
            self.cells_map = self.update_grid(nb_row, nb_col)
            print(self)
            print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    cell_map = CellMap('inputs/enigme1.txt')

    # 8 iterations
    start = time.time()

    cell_map.run_iterations(8)

    end = time.time()
    print(f"Execution time: {end - start}")
