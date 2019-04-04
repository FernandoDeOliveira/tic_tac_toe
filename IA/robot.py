import random
from env.frame import ROBOT_MOV, AGENT_MOV, FREE_CELL, TicTacToe


class Robot():
    def __init__(self):
        self.cell1 = 0
        self.cell2 = 0
        self.cell3 = 0
        self.cell4 = 0
        self.cell5 = 0
        self.cell6 = 0
        self.cell7 = 0
        self.cell8 = 0
        self.cell9 = 0
        self.memoria = [self.cell1, self.cell2, self.cell3,
                        self.cell4, self.cell5, self.cell6,
                        self.cell7, self.cell8, self.cell9]


    @property
    def memoria(self):
        return self._memoria


    @memoria.setter
    def memoria(self, frame):
        self._memoria = frame

    def check_env(self, TicTacToe):
        self.memoria = TicTacToe.frame


    def play(self, TicTacToe):
        "if first playng"
        if all(cell == FREE_CELL for cell in self.memoria):
            cell = random.sample([1, 3, 7, 9], 1)
            self.change_env(TicTacToe, cell)
        else:
            free_cells = self.check_free_cells()
            robot_played = self.robot_played()
            for played in robot_played:
                if played == 1:






    def change_env(self, TicTaeToe, cell):
        TicTaeToe.change(cell, ROBOT_MOV)

    def check_side_cell(self, cell):
        if cell == 1:
            return [2, 4, 5]
        elif cell == 2:
            return [1, 3, 4, 5, 6]
        elif cell == 3:
            return [2, 5, 6]
        elif cell == 4:
            return [1, 2, 5, 7, 8]
        elif cell == 5:
            return [1, 2, 3, 4, 6, 7, 8, 9]
        elif cell == 6:
            return [2, 3, 5, 8, 9]
        elif cell == 7:
            return [4, 5, 8]
        elif cell == 8:
            return [4, 5, 6, 7, 9]
        elif cell == 9:
            return [5, 6, 8]

    def robot_played(self):
        robot_move_on = []
        for i, cell in enumerate(self.memoria):
            if cell == ROBOT_MOV:
                robot_move_on.append(i)



    def check_free_cells(self):
        free_cells = []
        for i, cell in enumerate(self.memoria):
            if cell == FREE_CELL:
                free_cells.append(i)
        return free_cells





t = TicTacToe()
t.change(3, 2)

r = Robot()
print(r.memoria)
