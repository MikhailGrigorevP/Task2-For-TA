cells = {' ': 'EMPTY',
         'c': 'CONCRETE',
         'w': 'WOOD',
         'p': 'PLASTIC',
         'g': 'GLASS',
         's': 'STEEL',
         'e': 'EXIT'}

cell_type = {'EMPTY': 0,
             'CONCRETE': 4,
             'WOOD': 3,
             'PLASTIC': 2,
             'GLASS': 1,
             'STEEL': 5,
             'EXIT': 100, }

look = {'0': 'right',
        '1': 'down',
        '2': 'left',
        '3': 'up',
        }


class Cell:
    def __init__(self, _type):
        self.type = _type.split('-')
        self.solidity = []
        for t in self.type:
            self.solidity.append(cell_type[t])

    def __repr__(self):
        return self.solidity


class Robot:
    def __init__(self, x, y, turn, power, _map):
        # power - drill power
        # turn - turning direction
        self.x = x
        self.y = y
        self.turn = turn
        self.power = power
        self.map = _map
        self.wall = ['CONCRETE', 'WOOD', 'PLASTIC', 'GLASS', 'STEEL']

    def __repr__(self):
        return f'''\n x = {self.x}\n y = {self.y}\n turn: {look[str(self.turn)]}\n Drill power: {self.power}'''

    def show(self):
        for row in self.map:
            for cell in row:
                print(cell.solidity, end=' ')
            print()

    def scan_next(self, turn=0):
        if turn == 0:
            return self.map[self.y][self.x + 1]
        if turn == 1:
            return self.map[self.y + 1][self.x]
        if turn == 2:
            return self.map[self.y][self.x - 1]
        if turn == 3:
            return self.map[self.y - 1][self.x]

    def forward(self):
        if self.turn == 0:
            if self.scan_next(0).type in self.wall:
                return True
            else:
                self.x += 1
                return False
        if self.turn == 1:
            if self.scan_next(1).type in self.wall:
                return True
            else:
                self.y += 1
                return False
        if self.turn == 2:
            if self.scan_next(2).type in self.wall:
                return True
            else:
                self.x -= 1
                return False
        if self.turn == 3:
            if self.scan_next(3).type in self.wall:
                return True
            else:
                self.y -= 1
                return False

    def back(self):
        if self.turn == 0:
            if self.scan_next(2).type in self.wall:
                return True
            else:
                self.x -= 1
                return False
        if self.turn == 1:
            if self.scan_next(3).type in self.wall:
                return True
            else:
                self.y -= 1
                return False
        if self.turn == 2:
            if self.scan_next(0).type in self.wall:
                return True
            else:
                self.x += 1
                return False
        if self.turn == 3:
            if self.scan_next(1).type in self.wall:
                return True
            else:
                self.y += 1
                return False

    def left(self):
        if self.turn == 0:
            if self.scan_next(3).type in self.wall:
                return True
            else:
                self.y -= 1
                return False
        if self.turn == 1:
            if self.scan_next(0).type in self.wall:
                return True
            else:
                self.x += 1
                return False
        if self.turn == 2:
            if self.scan_next(1).type in self.wall:
                return True
            else:
                self.y += 1
                return False
        if self.turn == 3:
            if self.scan_next(2).type in self.wall:
                return True
            else:
                self.x -= 1
                return False

    def right(self):
        if self.turn == 0:
            if self.scan_next(1).type in self.wall:
                return True
            else:
                self.y += 1
                return False
        if self.turn == 1:
            if self.scan_next(2).type in self.wall:
                return True
            else:
                self.x -= 1
                return False
        if self.turn == 2:
            if self.scan_next(3).type in self.wall:
                return True
            else:
                self.y -= 1
                return False
        if self.turn == 3:
            if self.scan_next(0).type in self.wall:
                return True
            else:
                self.x += 1
                return False

    def rotate_right(self):
        self.turn = (self.turn + 1) % 4
        return True

    def rotate_left(self):
        self.turn = (self.turn - 1) % 4
        return True

    def lms(self):
        if self.turn == 0:
            distance = 1
            while self.map[self.y][self.x + distance].type[0] == "EMPTY":
                distance += 1
            return distance - 1
        if self.turn == 1:
            distance = 1
            while self.map[self.y + distance][self.x].type[0] == "EMPTY":
                distance += 1
            return distance - 1
        if self.turn == 2:
            distance = 1
            while self.map[self.y][self.x - distance].type[0] == "EMPTY":
                distance += 1
            return distance - 1
        if self.turn == 3:
            distance = 1
            while self.map[self.y - distance][self.x].type[0] == "EMPTY":
                distance += 1
            return distance - 1

    def drill(self):
        if self.turn == 0:
            if self.x == len(self.map[0])-2:
                self.power = 0
                return 0
            if self.power > self.scan_next(0).solidity[0]:
                self.power -= self.scan_next(0).solidity[0]
                if len(self.map[self.y][self.x + 1].type) == 1:
                    self.map[self.y][self.x + 1].solidity[0] = 0
                    self.map[self.y][self.x + 1].type[0] = "EMPTY"
                else:
                    self.map[self.y][self.x + 1].solidity.pop(0)
                    self.map[self.y][self.x + 1].type.pop(0)
            else:
                self.power = 0
            return self.power
        if self.turn == 1:
            if self.y == len(self.map)-2:
                self.power = 0
                return 0
            if self.power > self.scan_next(1).solidity[0]:
                self.power -= self.scan_next(1).solidity[0]
                if len(self.map[self.y + 1][self.x].type) == 1:
                    self.map[self.y + 1][self.x].solidity[0] = 0
                    self.map[self.y + 1][self.x].type[0] = "EMPTY"
                else:
                    self.map[self.y + 1][self.x].solidity.pop(0)
                    self.map[self.y + 1][self.x].type.pop(0)
            else:
                self.power = 0
            return self.power
        if self.turn == 2:
            if self.x == 1:
                self.power = 0
                return 0
            if self.power > self.scan_next(2).solidity[0]:
                self.power -= self.scan_next(2).solidity[0]
                if len(self.map[self.y][self.x - 1].type) == 1:
                    self.map[self.y][self.x - 1].solidity[0] = 0
                    self.map[self.y][self.x - 1].type[0] = "EMPTY"
                else:
                    self.map[self.y][self.x - 1].solidity.pop(0)
                    self.map[self.y][self.x - 1].type.pop(0)
            else:
                self.power = 0
            return self.power
        if self.turn == 3:
            if self.y == 1:
                self.power = 0
                return 0
            if self.power > self.scan_next(3).solidity[0]:
                self.power -= self.scan_next(3).solidity[0]
                if len(self.map[self.y - 1][self.x].type) == 1:
                    self.map[self.y -1][self.x].solidity[0] = 0
                    self.map[self.y - 1][self.x].type[0] = "EMPTY"
                else:
                    self.map[self.y -1][self.x].solidity.pop(0)
                    self.map[self.y - 1][self.x].type.pop(0)

            else:
                self.power = 0
            return self.power

    def reflect(self):
        if self.turn == 0:
            return self.map[self.y][self.x + self.lms() + 1].type[0]
        if self.turn == 1:
            return self.map[self.y + self.lms() + 1][self.x].type[0]
        if self.turn == 2:
            return self.map[self.y][self.x - self.lms() - 1].type[0]
        if self.turn == 3:
            return self.map[self.y - self.lms() - 1][self.x].type[0]
