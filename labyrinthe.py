class Labyrinthe:
    def __init__(self):

        self.structure = [
            [["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""],
             ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""],
             ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""]],
            [["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""], ["pierre", "lierre", ""], ["pierre", "", ""],
             ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""],
             ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""]],
            [["pierre", "", ""], ["pierre", "", ""], ["0", "", ""], ["0", "", ""], ["0", "", ""], ["pierre", "", ""],
             ["0", "", ""], ["0", "", ""], ["0", "", ""], ["pierre", "lierre", ""], ["pierre", "porte", ""],
             ["pierre", "", ""], ["pierre", "", ""]],
            [["pierre", "", ""], ["pierre", "", ""], ["0", "", ""], ["pierre", "", ""], ["0", "", ""], ["0", "", ""],
             ["0", "", ""], ["pierre", "lierre", ""], ["0", "", ""], ["pierre", "lierre", ""], ["0", "", ""], ["pierre", "", ""],
             ["pierre", "", ""]],
            [["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""], ["0", "", ""],
             ["pierre", "", ""], ["0", "", ""], ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""],
             ["0", "", ""], ["pierre", "lierre", ""], ["pierre", "", ""]],
            [["pierre", "", ""], ["pierre", "", ""], ["0", "", ""], ["0", "", ""], ["0", "", ""], ["0", "", ""],
             ["0", "", ""], ["pierre", "lierre", ""], ["0", "", ""], ["0", "", ""], ["0", "", ""], ["pierre", "", ""],
             ["pierre", "", ""]],
            [["pierre", "", ""], ["pierre", "lierre", ""], ["0", "", ""], ["pierre", "lierre", ""], ["pierre", "", ""],
             ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""], ["0", "", ""], ["pierre", "", ""],
             ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""]],
            [["pierre", "", ""], ["pierre", "", ""], ["0", "", ""], ["pierre", "lierre", ""], ["0", "", ""], ["0", "", ""],
             ["0", "", ""], ["pierre", "lierre", ""], ["0", "", ""], ["pierre", "", ""], ["0", "", ""], ["pierre", "", ""],
             ["pierre", "", ""]],
            [["pierre", "", ""], ["pierre", "", ""], ["0", "", ""], ["0", "", ""], ["0", "", ""], ["pierre", "", ""],
             ["0", "", ""], ["0", "", ""], ["0", "", ""], ["pierre", "", ""], ["0", "", ""], ["pierre", "", ""],
             ["pierre", "", ""]],
            [["pierre", "", ""], ["pierre", "", ""], ["0", "", ""], ["pierre", "", ""], ["pierre", "", ""],
             ["pierre", "", ""], ["0", "", ""], ["pierre", "", ""], ["0", "", ""], ["0", "", ""], ["0", "", ""],
             ["pierre", "", ""], ["pierre", "", ""]],
            [["pierre", "", ""], ["pierre", "", ""], ["0", "", ""], ["0", "", ""], ["pierre", "", ""], ["0", "", ""],
             ["0", "", ""], ["pierre", "", ""], ["0", "", ""], ["pierre", "", ""], ["0", "", ""], ["pierre", "", ""],
             ["pierre", "", ""]],
            [["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""],
             ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""],
             ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""]],
            [["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""],
             ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""],
             ["pierre", "", ""], ["pierre", "", ""], ["pierre", "", ""]]]

        '''self.structure = [[['pierre', '', ''], ['pierre', '', ''], ['pierre', '', ''], ['pierre', '', ''], ['pierre', '', ''], ['pierre', '', ''], ['pierre', '', '']],
                          [['pierre', '', ''], ['pierre', '', ''], ['pierre', '', ''], ['pierre', '', ''], ['pierre', '', ''], ['pierre', '', ''], ['pierre', '', '']],
                          [['pierre', '', ''], ['pierre', '', ''], ['0', '', ''], ['0', '', ''], ['pierre', 'porte', ''], ['pierre', '', ''], ['pierre', '', '']],
                          [['pierre', '', ''], ['pierre', '', ''], ['0', '', ''], ['pierre', '', ''], ['pierre', '', ''], ['pierre', '', ''], ['pierre', '', '']],
                          [['pierre', '', ''], ['pierre', '', ''], ['0', '', ''], ['pierre', '', ''], ['pierre', '', ''], ['pierre', '', ''], ['pierre', '', '']],
                          [['pierre', '', ''], ['pierre', '', ''], ['pierre', '', ''], ['pierre', '', ''], ['pierre', '', ''], ['pierre', '', ''], ['pierre', '', '']],
                          [['pierre', '', ''], ['pierre', '', ''], ['pierre', '', ''], ['pierre', '', ''], ['pierre', '', ''], ['pierre', '', ''], ['pierre', '', '']]]'''

    def vue(self):
        print(self.structure[2])
        player_line = self.structure[2]
        player_row = 0
        for i in range(player_row - 0, player_row + 2, 0):
            vue = player_line[i]
        print(vue)



