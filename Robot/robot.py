from Robot import map


class robot:
    def __init__(self, x, y, turn, power, _map):
        # power - drill power
        # turn - turning direction
        # 0 -right
        # 1 - down
        # 2 - left
        # 3 - up
        self.x = x
        self.y = y
        self.turn = turn
        self.power = power
        self.map = _map
        self.wall = ['CONCRETE', 'WOOD', 'PLASTIC', 'GLASS', 'STEEL']

    def __repr__(self):
        return f'''({self.x}, {self.y}):{self.turn}\n
                Drill power: {self.power}'''

    def scan_next(self, turn=0):
        if turn == 0:
            return self.map[self.y][self.x + 1]
        if turn == 1:
            return self.map[self.y - 1][self.x]
        if turn == 2:
            return self.map[self.y][self.x - 1]
        if turn == 3:
            return self.map[self.y + 1][self.x]

    def forward(self):
        if self.turn == 0:
            if self.scan_next(0).type.type in self.wall:
                return True
            else:
                self.x += 1
                return False
        if self.turn == 1:
            if self.scan_next(1).type.type in self.wall:
                return True
            else:
                self.y -= 1
                return False
        if self.turn == 2:
            if self.scan_next(2).type.type in self.wall:
                return True
            else:
                self.x -= 1
                return False
        if self.turn == 3:
            if self.scan_next(3).type.type in self.wall:
                return True
            else:
                self.y += 1
                return False

    def back(self):
        if self.turn == 0:
            if self.scan_next(2).type.type in self.wall:
                return True
            else:
                self.x -= 1
                return False
        if self.turn == 1:
            if self.scan_next(3).type.type in self.wall:
                return True
            else:
                self.y += 1
                return False
        if self.turn == 2:
            if self.scan_next(0).type.type in self.wall:
                return True
            else:
                self.x += 1
                return False
        if self.turn == 3:
            if self.scan_next(1).type.type in self.wall:
                return True
            else:
                self.y -= 1
                return False

    def left(self):
        if self.turn == 0:
            if self.scan_next(3).type.type in self.wall:
                return True
            else:
                self.y += 1
                return False
        if self.turn == 1:
            if self.scan_next(0).type.type in self.wall:
                return True
            else:
                self.x += 1
                return False
        if self.turn == 2:
            if self.scan_next(1).type.type in self.wall:
                return True
            else:
                self.y -= 1
                return False
        if self.turn == 3:
            if self.scan_next(2).type.type in self.wall:
                return True
            else:
                self.x -= 1
                return False

    def right(self):
        if self.turn == 0:
            if self.scan_next(1).type.type in self.wall:
                return True
            else:
                self.y -= 1
                return False
        if self.turn == 1:
            if self.scan_next(2).type.type in self.wall:
                return True
            else:
                self.x -= 1
                return False
        if self.turn == 2:
            if self.scan_next(3).type.type in self.wall:
                return True
            else:
                self.y += 1
                return False
        if self.turn == 3:
            if self.scan_next(0).type.type in self.wall:
                return True
            else:
                self.x += 1
                return False

    def rotate_right(self):
        self.turn = (self.turn + 1) % 4
        return True

    def rotate_left(self):
        self.turn = (abs(self.turn - 1)) % 4
        return True

    def lms(self):
        if self.turn == 0:
            distance = 1
            while self.map[self.y][self.x + distance].type.type == "EMPTY":
                distance += 1
            return distance - 1
        if self.turn == 1:
            distance = 1
            while self.map[self.y - distance][self.x].type.type == "EMPTY":
                distance += 1
            return distance - 1
        if self.turn == 2:
            distance = 1
            while self.map[self.y][self.x - distance].type.type == "EMPTY":
                distance += 1
            return distance - 1
        if self.turn == 3:
            distance = 1
            while self.map[self.y + distance][self.x].type.type == "EMPTY":
                distance += 1
            return distance - 1

    def drill(self):
        if self.turn == 0:
            if self.power > self.scan_next(0).type.solidify:
                self.power -= self.scan_next(0).type.solidify
                self.map[self.y][self.x + 1].type.solidify = 0
                self.map[self.y][self.x + 1].type.type = "EMPTY"
            else:
                self.power = 0
            return self.power
        if self.turn == 1:
            if self.power > self.scan_next(1).type.solidify:
                self.power -= self.scan_next(1).type.solidify
                self.map[self.y - 1][self.x].type.solidify = 0
                self.map[self.y - 1][self.x].type.type = "EMPTY"
            else:
                self.power = 0
            return self.power
        if self.turn == 2:
            if self.power > self.scan_next(2).type.solidify:
                self.power -= self.scan_next(2).type.solidify
                self.map[self.y][self.x - 1].type.solidify = 0
                self.map[self.y][self.x - 1].type.type = "EMPTY"
            else:
                self.power = 0
            return self.power
        if self.turn == 3:
            if self.power > self.scan_next(3).type.solidify:
                self.power -= self.scan_next(3).type.solidify
                self.map[self.y + 1][self.x].type.solidify = 0
                self.map[self.y + 1][self.x].type.type = "EMPTY"
            else:
                self.power = 0
            return self.power

    def reflect(self):
        if self.turn == 0:
            return self.map[self.y][self.x + self.lms() + 1].type.type
        if self.turn == 1:
            return self.map[self.y - self.lms() - 1][self.x].type.type
        if self.turn == 2:
            return self.map[self.y][self.x - self.lms() - 1].type.type
        if self.turn == 3:
            return self.map[self.y + self.lms() + 1][self.x].type.type
