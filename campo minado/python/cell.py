def Cell(i, j, w):
    Self.i = i
    self.j = j
    self.x = i*w
    self.w = j*w
    self.neighborCount = 0

    self.bomb = False
    self.reveled = False
