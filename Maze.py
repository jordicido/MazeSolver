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
            cell = Cell(offset_x, offset_y, offset_x+self.cell_size_x, offset_y+self.cell_size_y, self.win)
    
        cell.draw()
        if self.win != None:
            self._animate()
        return cell
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[len(self._cells)-1][len(self._cells[0])-1].has_bottom_wall = False
        self._draw_cell(0, 0, self._cells[0][0])
        self._draw_cell(0, 0, self._cells[len(self._cells)-1][len(self._cells[0])-1])
