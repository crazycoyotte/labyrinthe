import labyrinthe


class Labyrinthe:
    def __init__(self):
        self.structure = [["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
                          ["1", "0", "0", "0", "1", "0", "0", "0", "1", "2", "1"],
                          ["1", "0", "1", "0", "0", "0", "1", "0", "1", "0", "1"],
                          ["1", "1", "1", "0", "1", "0", "1", "1", "1", "0", "1"],
                          ["1", "0", "0", "0", "0", "0", "1", "0", "0", "0", "1"],
                          ["1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1"],
                          ["1", "0", "1", "0", "0", "0", "1", "0", "1", "0", "1"],
                          ["1", "0", "0", "0", "1", "0", "0", "0", "1", "0", "1"],
                          ["1", "0", "1", "1", "1", "0", "1", "0", "0", "0", "1"],
                          ["1", "0", "0", "1", "0", "0", "1", "0", "1", "0", "1"],
                          ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
                          ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]]

    def vue(self):
        print(self.structure[2])
        player_line = self.structure[2]
        player_row = 0
        for i in range(player_row - 0, player_row + 2, 0):
            vue = player_line[i]
        print(vue)

laby = labyrinthe.Labyrinthe()

