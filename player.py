
class Player:

    def __init__(self):
        self.pos_x = 1
        self.pos_y = 1
        self.orientation = 2
        self.victory = False

    def move2(self, delta_x, delta_y, laby):
        move = False
        player_line = laby.structure[self.pos_y + delta_y]
        if player_line[self.pos_x + delta_x] == "▢":
            move = True
        elif player_line[self.pos_x + delta_x] == "▒":
            self.victory = True

        if move:
            self.pos_y += delta_y
            self.pos_x += delta_x
        return self
