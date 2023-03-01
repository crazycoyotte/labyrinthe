def move_y(delta_y, actual_x, actual_y, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, victory):
    y_move = False
    if actual_y + delta_y == 0:
        if line0[actual_x] == "▢":
            y_move = True
        elif line0[actual_x] == "▒":
            victory = True
    if actual_y + delta_y == 1:
        if line1[actual_x] == "▢":
            y_move = True
        elif line1[actual_x] == "▒":
            victory = True
    if actual_y + delta_y == 2:
        if line2[actual_x] == "▢":
            y_move = True
        elif line2[actual_x] == "▒":
            victory = True
    if actual_y + delta_y == 3:
        if line3[actual_x] == "▢":
            y_move = True
        elif line3[actual_x] == "▒":
            victory = True
    if actual_y + delta_y == 4:
        if line4[actual_x] == "▢":
            y_move = True
        elif line4[actual_x] == "▒":
            victory = True
    if actual_y + delta_y == 5:
        if line5[actual_x] == "▢":
            y_move = True
        elif line5[actual_x] == "▒":
            victory = True
    if actual_y + delta_y == 6:
        if line6[actual_x] == "▢":
            y_move = True
        elif line6[actual_x] == "▒":
            victory = True
    if actual_y + delta_y == 7:
        if line7[actual_x] == "▢":
            y_move = True
        elif line7[actual_x] == "▒":
            victory = True
    if actual_y + delta_y == 8:
        if line8[actual_x] == "▢":
            y_move = True
        elif line8[actual_x] == "▒":
            victory = True
    if actual_y + delta_y == 9:
        if line9[actual_x] == "▢":
            y_move = True
        elif line9[actual_x] == "▒":
            victory = True
    if actual_y + delta_y == 10:
        if line10[actual_x] == "▢":
            y_move = True
        elif line10[actual_x] == "▒":
            victory = True
    if y_move:
        actual_y += delta_y
    liste_y = [actual_y, victory]
    return liste_y


def move_x(delta_x, actual_x, actual_y, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, victory):
    x_move = False
    if actual_y == 0:
        if line0[actual_x + delta_x] == "▢":
            x_move = True
    if actual_y == 1:
        if line1[actual_x + delta_x] == "▢":
            x_move = True
    if actual_y == 2:
        if line2[actual_x + delta_x] == "▢":
            x_move = True
    if actual_y == 3:
        if line3[actual_x + delta_x] == "▢":
            x_move = True
    if actual_y == 4:
        if line4[actual_x + delta_x] == "▢":
            x_move = True
    if actual_y == 5:
        if line5[actual_x + delta_x] == "▢":
            x_move = True
    if actual_y == 6:
        if line6[actual_x + delta_x] == "▢":
            x_move = True
    if actual_y == 7:
        if line7[actual_x + delta_x] == "▢":
            x_move = True
    if actual_y == 8:
        if line8[actual_x + delta_x] == "▢":
            x_move = True
    if actual_y == 9:
        if line9[actual_x + delta_x] == "▢":
            x_move = True
    if actual_y == 10:
        if line10[actual_x + delta_x] == "▢":
            x_move = True

    if x_move:
        actual_x += delta_x
    liste_x = [actual_x, victory]
    return liste_x

