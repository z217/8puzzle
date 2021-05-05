class Node(object):
    def __init__(self, stat: list[list[int]], f: int, g: int, h: int, cID: int, pID: int):
        self.stat = []
        for i in stat:
            self.stat.append(i[:])
        self.f = f
        self.g = g
        self.h = h
        self.cID = cID
        self.pID = pID
