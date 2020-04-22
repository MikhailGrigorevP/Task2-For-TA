from __future__ import annotations
from typing import List, Dict, Optional


class node(object):
    # object constructor
    def __init__(self, t='const', val=None, ch: Optional[List[node]] = None):
        self.type = t
        self.value = val
        self.child = ch
        self.acc = None

    # object representation
    def __repr__(self):
        return f'{self.type} {self.value}'

    # print Tree
    def print(self, lvl=0):
        # offset
        print(' ' * lvl, ' ', self)
        if self.child is not None:
            if isinstance(self.child, node):
                self.child.print(lvl + 1)
            elif isinstance(self.child, str):
                print(' ' * (lvl + 1), self.child)
            elif isinstance(self.child, list):
                for i in range(len(self.child)):
                    if isinstance(self.child[i], str):
                        print(' ' * (lvl + 1), self.child[i])
                    else:
                        self.child[i].print(lvl + 1)
            elif isinstance(self.child, dict):
                for key, value in self.child.items():
                    print(' ' * (lvl + 1), key)
                    if isinstance(value, str):
                        print(' ' * (lvl + 2), value)
                    elif isinstance(value, node):
                        value.print(lvl + 2)
