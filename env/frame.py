
ROBOT_MOV = 1
AGENT_MOV = 2
FREE_CELL = 0


class TicTacToe:

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

    @property
    def frame(self):
        return [self.cell1, self.cell2, self.cell3,
                self.cell4, self.cell5, self.cell6,
                self.cell7, self.cell8, self.cell9]


    def change(self,cell, to):
        command = "self.cell{} = {}".format(cell, to)
        exec(command)


    def print_(self):
        frame = ['', '', '',
                 '', '', '',
                 '', '', '']

        for i, cell in enumerate(self.frame):
            if cell == 0:
                frame[i] = '_'
            elif cell == 1:
                frame[i] = 'X'
            elif cell == 2:
                frame[i] = 'O'

        table = """
        {cell1} | {cell2} | {cell3}
        {cell4} | {cell5} | {cell6}
        {cell7} | {cell8} | {cell9}
        
        """.format(cell1=frame[0], cell2=frame[1], cell3=frame[2],
                   cell4=frame[3], cell5=frame[4], cell6=frame[5],
                   cell7=frame[6], cell8=frame[7], cell9=frame[8])
        print(self.frame)
        print(table)


t = TicTacToe()
t.change(5, 2)

t.print_()

