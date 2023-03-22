class Player:

    def __init__(self):
        self.pos_x = 2
        self.pos_y = 2
        self.victory = False

    def move2(self, delta_x, delta_y, laby):
        move = False
        player_line = laby.structure[self.pos_y + delta_y]
        line_0y = laby.structure[self.pos_y]
        line_m1y = laby.structure[self.pos_y - 1]
        line_p1y = laby.structure[self.pos_y + 1]
        case_0y_0x = player_line[self.pos_x]
        case_0y_p1x = line_0y[self.pos_x + 1]
        case_0y_m1x = line_0y[self.pos_x - 1]
        case_m1y_0x = line_m1y[self.pos_x]
        case_p1y_0x = line_p1y[self.pos_x]
        print(player_line[self.pos_x + delta_x])
        if delta_x == 1 and case_0y_p1x[0] == "0":
            move = True
        if delta_x == -1 and case_0y_m1x[0] == "0":
            move = True
        if delta_y == 1 and case_p1y_0x[0] == "0":
            move = True
        if delta_y == -1 and case_m1y_0x[0] == "0":
            move = True
        '''if player_line[self.pos_x + delta_x] == "0":
            move = True
        elif player_line[self.pos_x + delta_x] == "2":
            self.victory = True'''

        if move:
            self.pos_y += delta_y
            self.pos_x += delta_x
        return self
