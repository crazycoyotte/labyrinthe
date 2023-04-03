class Case:

    def __init__(self, pos_x, pos_y, sprite, deco) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.sprite = sprite
        self.deco = deco

    def __repr__(self):
        t = f"x : {self.pos_x}, y = {self.pos_y}, sprite = {self.sprite}, deco = {self.deco}"
        