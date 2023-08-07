import random
from Cell import Cell
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
        if seed != None:
            self.seed = random.seed(seed)
        else:
            self.seed = random.seed(0)
        self._break_walls_r(0,0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        for i in range(self.num_cols):
            row_of_cells = []
            for j in range(self.num_rows):
                row_of_cells.append(self._draw_cell(i, j))
            self._cells.append(row_of_cells)
        
        self._break_entrance_and_exit()

    def _draw_cell(self, i, j, cell=None):
        if cell == None:
            offset_x = self.x1 + self.cell_size_x*j+2
            offset_y = self.y1 + self.cell_size_y*i+2
            cell = Cell(offset_x, offset_y, offset_x+self.cell_size_x, offset_y+self.cell_size_y, False, self.win)
    
        if self.win != None:
            cell.draw()
            self._animate()
        return cell
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[len(self._cells)-1][len(self._cells[0])-1].has_bottom_wall = False
        self._cells[len(self._cells)-1][len(self._cells[0])-1].end = True
        self._draw_cell(0, 0, self._cells[0][0])
        self._draw_cell(0, 0, self._cells[len(self._cells)-1][len(self._cells[0])-1])
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        cells_to_visit = True

        while cells_to_visit:
            to_visit = []
            if i - 1 > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))
            if j - 1 > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))
            if j + 1 < len(self._cells[i]) and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))
            if i + 1 < len(self._cells) and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))

            if len(to_visit) == 0:
                self._draw_cell(0, 0, self._cells[i][j])
                return
            else:
                random_cell = to_visit[random.randrange(len(to_visit))]
                if random_cell[0] == i - 1:
                    self._cells[i][j].has_top_wall = False
                    self._cells[random_cell[0]][random_cell[1]].has_bottom_wall = False
                elif random_cell[0] == i + 1:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[random_cell[0]][random_cell[1]].has_top_wall = False
                elif random_cell[1] == j - 1:
                    self._cells[i][j].has_left_wall = False
                    self._cells[random_cell[0]][random_cell[1]].has_right_wall = False
                else:
                    self._cells[i][j].has_right_wall = False
                    self._cells[random_cell[0]][random_cell[1]].has_left_wall = False
            
                self._break_walls_r(random_cell[0], random_cell[1])
    
    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited = False
    
    def solve(self):
        return self._solve_r(0,0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if self._cells[i][j].end:
            return True
    
        if i - 1 > 0 and not self._cells[i-1][j].visited and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            result = self._solve_r(i-1, j)
            if result:
                return True
            self._cells[i-1][j].draw_move(self._cells[i][j], True)
        if j - 1 > 0 and not self._cells[i][j-1].visited and not self._cells[i][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            result = self._solve_r(i, j-1)
            if result:
                return True
            self._cells[i][j-1].draw_move(self._cells[i][j], True)
        if j + 1 < len(self._cells[i]) and not self._cells[i][j+1].visited and not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            result = self._solve_r(i, j+1)
            if result:
                return True
            self._cells[i][j+1].draw_move(self._cells[i][j], True)
        if i + 1 < len(self._cells) and not self._cells[i+1][j].visited and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            result = self._solve_r(i+1, j)
            if result:
                return True
            self._cells[i+1][j].draw_move(self._cells[i][j], True)
        

        return False    