class Player:

    def __init__(self):
        self.pos_x = 1
        self.pos_y = 1
        self.orientation = 2
        self.victory = False

    def move2(self, delta_x, delta_y, line0, line1, line2, line3, line4, line5, line6, line7, line8,
              line9, line10):
        move = False
        if self.pos_y + delta_y == 0:
            if line0[self.pos_x + delta_x] == "▢":
                move = True
            elif line0[self.pos_x + delta_x] == "▒":
                self.victory = True
        if self.pos_y + delta_y == 1:
            if line1[self.pos_x + delta_x] == "▢":
                move = True
            elif line1[self.pos_x + delta_x] == "▒":
                self.victory = True
        if self.pos_y + delta_y == 2:
            if line2[self.pos_x + delta_x] == "▢":
                move = True
            elif line2[self.pos_x + delta_x] == "▒":
                self.victory = True
        if self.pos_y + delta_y == 3:
            if line3[self.pos_x + delta_x] == "▢":
                move = True
            elif line3[self.pos_x + delta_x] == "▒":
                self.victory = True
        if self.pos_y + delta_y == 4:
            if line4[self.pos_x + delta_x] == "▢":
                move = True
            elif line4[self.pos_x + delta_x] == "▒":
                self.victory = True
        if self.pos_y + delta_y == 5:
            if line5[self.pos_x + delta_x] == "▢":
                move = True
            elif line5[self.pos_x + delta_x] == "▒":
                self.victory = True
        if self.pos_y + delta_y == 6:
            if line6[self.pos_x + delta_x] == "▢":
                move = True
            elif line6[self.pos_x + delta_x] == "▒":
                self.victory = True
        if self.pos_y + delta_y == 7:
            if line7[self.pos_x + delta_x] == "▢":
                move = True
            elif line7[self.pos_x + delta_x] == "▒":
                self.victory = True
        if self.pos_y + delta_y == 8:
            if line8[self.pos_x + delta_x] == "▢":
                move = True
            elif line8[self.pos_x + delta_x] == "▒":
                self.victory = True
        if self.pos_y + delta_y == 9:
            if line9[self.pos_x + delta_x] == "▢":
                move = True
            elif line9[self.pos_x + delta_x] == "▒":
                self.victory = True
        if self.pos_y + delta_y == 10:
            if line10[self.pos_x + delta_x] == "▢":
                move = True
            elif line10[self.pos_x + delta_x] == "▒":
                self.victory = True
        if move:
            self.pos_y += delta_y
            self.pos_x += delta_x
        return self
