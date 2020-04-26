class Cell:
    def __init__(self, x, y, _type, _solidity):
        self.x = x
        self.y = y
        self.type = _type
        self.solidity = _solidity

    def __repr__(self):
        return f'{self.x} {self.y} : {self.type}'


class CellType:
    type = 'cell'
    solidity = 0

    def __init__(self):
        pass

    def __repr__(self):
        return self.type


class Empty(CellType):
    type = 'EMPTY'
    solidity = 0


class Concrete(CellType):
    type = 'CONCRETE'
    solidity = 4


class Wood(CellType):
    type = 'WOOD'
    solidity = 3


class Plastic(CellType):
    type = 'PLASTIC'
    solidity = 2


class Glass(CellType):
    type = 'GLASS'
    solidity = 1


class Steel(CellType):
    type = 'STEEL'
    solidity = 5


class Exit(CellType):
    type = 'EXIT'
    solidity = 0