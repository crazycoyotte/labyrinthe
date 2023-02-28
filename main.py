# Import
import tkinter as tk

# position d'origine du joueur
pos_x = 1
pos_y = 1
victory = False

# Le labyrinth
line0 = ["■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"]
line1 = ["■", "▢", "▢", "▢", "■", "▢", "▢", "▢", "■", "▒", "■"]
line2 = ["■", "▢", "■", "▢", "▢", "▢", "■", "▢", "■", "▢", "■"]
line3 = ["■", "■", "■", "▢", "■", "▢", "■", "■", "■", "▢", "■"]
line4 = ["■", "▢", "▢", "▢", "■", "■", "■", "▢", "▢", "▢", "■"]
line5 = ["■", "▢", "■", "■", "■", "■", "■", "▢", "■", "■", "■"]
line6 = ["■", "▢", "■", "▢", "▢", "▢", "■", "▢", "■", "▢", "■"]
line7 = ["■", "▢", "▢", "▢", "■", "▢", "▢", "▢", "■", "▢", "■"]
line8 = ["■", "▢", "■", "■", "■", "▢", "■", "▢", "▢", "▢", "■"]
line9 = ["■", "▢", "▢", "■", "▢", "▢", "■", "▢", "■", "▢", "■"]
line10 = ["■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"]


# Fonctions
# Fonction appelée lors du clic sur le bouton
def move_y(delta_y):
    global pos_y, victory
    y_move = False
    if pos_y + delta_y == 1:
        if line1[pos_x] == "▢":
            y_move = True
        elif line1[pos_x] == "▒":
            victory = True
    if pos_y + delta_y == 2:
        if line2[pos_x] == "▢":
            y_move = True
        elif line2[pos_x] == "▒":
            victory = True
    if pos_y + delta_y == 3:
        if line3[pos_x] == "▢":
            y_move = True
        elif line3[pos_x] == "▒":
            victory = True
    if pos_y + delta_y == 4:
        if line4[pos_x] == "▢":
            y_move = True
        elif line4[pos_x] == "▒":
            victory = True
    if pos_y + delta_y == 5:
        if line5[pos_x] == "▢":
            y_move = True
        elif line5[pos_x] == "▒":
            victory = True
    if pos_y + delta_y == 6:
        if line6[pos_x] == "▢":
            y_move = True
        elif line6[pos_x] == "▒":
            victory = True
    if pos_y + delta_y == 7:
        if line7[pos_x] == "▢":
            y_move = True
        elif line7[pos_x] == "▒":
            victory = True
    if pos_y + delta_y == 8:
        if line8[pos_x] == "▢":
            y_move = True
        elif line8[pos_x] == "▒":
            victory = True
    if pos_y + delta_y == 9:
        if line9[pos_x] == "▢":
            y_move = True
        elif line9[pos_x] == "▒":
            victory = True
    if pos_y + delta_y == 10:
        if line10[pos_x] == "▢":
            y_move = True
        elif line10[pos_x] == "▒":
            victory = True
    if y_move:
        pos_y += delta_y

    update_label()


def move_x(delta_x):
    global pos_x, pos_y, victory
    x_move = False
    if pos_y == 1:
        if line1[pos_x + delta_x] == "▢":
            x_move = True
    if pos_y == 2:
        if line2[pos_x + delta_x] == "▢":
            x_move = True
    if pos_y == 3:
        if line3[pos_x + delta_x] == "▢":
            x_move = True
    if pos_y == 4:
        if line4[pos_x + delta_x] == "▢":
            x_move = True
    if pos_y == 5:
        if line5[pos_x + delta_x] == "▢":
            x_move = True
    if pos_y == 6:
        if line6[pos_x + delta_x] == "▢":
            x_move = True
    if pos_y == 7:
        if line7[pos_x + delta_x] == "▢":
            x_move = True
    if pos_y == 8:
        if line8[pos_x + delta_x] == "▢":
            x_move = True
    if pos_y == 9:
        if line9[pos_x + delta_x] == "▢":
            x_move = True

    if x_move:
        pos_x += delta_x

    update_label()

def view():
    global pos_x, pos_y, victory
    if pos_y == 1:
        player_view = f"{line0[pos_x - 1]}{line0[pos_x]}{line0[pos_x + 1]}\n{line1[pos_x - 1]}◉{line1[pos_x + 1]}\n{line2[pos_x - 1]}{line2[pos_x]}{line2[pos_x + 1]}\n"
    if pos_y == 2:
        player_view = f"{line1[pos_x - 1]}{line1[pos_x]}{line1[pos_x + 1]}\n{line2[pos_x - 1]}◉{line2[pos_x + 1]}\n{line3[pos_x - 1]}{line3[pos_x]}{line3[pos_x + 1]}\n"
    if pos_y == 3:
        player_view = f"{line2[pos_x - 1]}{line2[pos_x]}{line2[pos_x + 1]}\n{line3[pos_x - 1]}◉{line3[pos_x + 1]}\n{line4[pos_x - 1]}{line4[pos_x]}{line4[pos_x + 1]}\n"
    if pos_y == 4:
        player_view = f"{line3[pos_x - 1]}{line3[pos_x]}{line3[pos_x + 1]}\n{line4[pos_x - 1]}◉{line4[pos_x + 1]}\n{line5[pos_x - 1]}{line5[pos_x]}{line5[pos_x + 1]}\n"
    if pos_y == 5:
        player_view = f"{line4[pos_x - 1]}{line4[pos_x]}{line4[pos_x + 1]}\n{line5[pos_x - 1]}◉{line5[pos_x + 1]}\n{line6[pos_x - 1]}{line6[pos_x]}{line6[pos_x + 1]}\n"
    if pos_y == 6:
        player_view = f"{line5[pos_x - 1]}{line5[pos_x]}{line5[pos_x + 1]}\n{line6[pos_x - 1]}◉{line6[pos_x + 1]}\n{line7[pos_x - 1]}{line7[pos_x]}{line7[pos_x + 1]}\n"
    if pos_y == 7:
        player_view = f"{line6[pos_x - 1]}{line6[pos_x]}{line6[pos_x + 1]}\n{line7[pos_x - 1]}◉{line7[pos_x + 1]}\n{line8[pos_x - 1]}{line8[pos_x]}{line8[pos_x + 1]}\n"
    if pos_y == 8:
        player_view = f"{line7[pos_x - 1]}{line7[pos_x]}{line7[pos_x + 1]}\n{line8[pos_x - 1]}◉{line8[pos_x + 1]}\n{line9[pos_x - 1]}{line9[pos_x]}{line9[pos_x + 1]}\n"
    if pos_y == 9:
        player_view = f"{line8[pos_x - 1]}{line8[pos_x]}{line8[pos_x + 1]}\n{line9[pos_x - 1]}◉{line9[pos_x + 1]}\n{line10[pos_x - 1]}{line10[pos_x]}{line10[pos_x + 1]}\n"
    if victory:
        player_view = "Victoire !"
    return player_view


def update_label():
    # Fonction appelée lorsque le bouton est pressé
    text = view()  # Appel de la fonction "view()" pour récupérer le texte généré
    label.configure(text=text, font=("Arial", 18))  # Mise à jour du texte affiché dans le widget "label"


# Création de la fenêtre principale
root = tk.Tk()

# affichage
# Ajout d'un widget Label contenant le texte "Texte d'origine" à la fenêtre
lab_view = view()
label = tk.Label(root, text=lab_view, font=("Arial", 18))
label.grid(row=1, column=1)

# boutons
# Ajout d'un widget Bouton à la fenêtre, qui appelle la fonction go_up lorsqu'il est pressé
button = tk.Button(root, text="▲", command=lambda: move_y(-1), width=10, height=2)
button.grid(row=0, column=1)
# Ajout d'un widget Bouton à la fenêtre, qui appelle la fonction go_down lorsqu'il est pressé
button = tk.Button(root, text="▼", command=lambda: move_y(1), width=10, height=2)
button.grid(row=2, column=1)
# Ajout d'un widget Bouton à la fenêtre, qui appelle la fonction go_left lorsqu'il est pressé
button = tk.Button(root, text="◀", command=lambda: move_x(-1), width=5, height=10)
button.grid(row=1, column=0)
# Ajout d'un widget Bouton à la fenêtre, qui appelle la fonction go_right lorsqu'il est pressé
button = tk.Button(root, text="▶", command=lambda: move_x(1), width=5, height=10)
button.grid(row=1, column=2)


# Définition de la taille et de la position de la fenêtre
# geometry("largeurxhauteur+x+y")
root.geometry("250x250+100+50")

# Boucle principale pour afficher la fenêtre
root.mainloop()