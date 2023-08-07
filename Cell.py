from Line import Line
from Point import Point


class Cell:
    def __init__(self, 
                 top_left_corner_x, 
                 top_left_corner_y,
                 bottom_right_corner_x, 
                 bottom_right_corner_y, 
                 win=None
    ):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = top_left_corner_x
        self._x2 = bottom_right_corner_x
        self._y1 = top_left_corner_y
        self._y2 = bottom_right_corner_y
        self.visited = False
        self._win = win
    
    def draw(self):
        left = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))            
        right = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))            
        top = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))            
        bottom = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))            

        if self.has_left_wall:
            self._win.draw_line(left, "black")
        else:
            self._win.draw_line(left, "white")
        if self.has_right_wall:
            self._win.draw_line(right, "black")
        else:
            self._win.draw_line(right, "white")
        if self.has_top_wall:
            self._win.draw_line(top, "black")
        else:
            self._win.draw_line(top, "white")
        if self.has_bottom_wall:
            self._win.draw_line(bottom, "black")
        else:
            self._win.draw_line(bottom, "white")

    def draw_move(self, to_cell, undo=False):
        move = Line(Point((self._x2+self._x1) // 2, (self._y2+self._y1) // 2), Point((to_cell._x2+to_cell._x1) // 2, (to_cell._y2+to_cell._y1) // 2))
        if not undo:
            self._win.draw_line(move, "red")
        else:
            self._win.draw_line(move, "grey")