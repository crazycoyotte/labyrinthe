# Import
import tkinter as tk
import player


# instanciation du joueur
avatar = player.Player()

# Le labyrinth
line0 = ["■", "■", "■", "■", "■", "■", "■", "■", "■", "▒", "■"]
line1 = ["■", "▢", "▢", "▢", "■", "▢", "▢", "▢", "■", "▢", "■"]
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
def move(x, y):
    avatar.move2(x, y, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10)
    update_label()


def view():
    player_view = ""
    if avatar.pos_y == 1:
        player_view = f'''{line0[avatar.pos_x - 1]}{line0[avatar.pos_x]}{line0[avatar.pos_x + 1]}
{line1[avatar.pos_x - 1]}◉{line1[avatar.pos_x + 1]}
{line2[avatar.pos_x - 1]}{line2[avatar.pos_x]}{line2[avatar.pos_x + 1]}'''
    if avatar.pos_y == 2:
        player_view = f'''{line1[avatar.pos_x - 1]}{line1[avatar.pos_x]}{line1[avatar.pos_x + 1]}
{line2[avatar.pos_x - 1]}◉{line2[avatar.pos_x + 1]}
{line3[avatar.pos_x - 1]}{line3[avatar.pos_x]}{line3[avatar.pos_x + 1]}'''
    if avatar.pos_y == 3:
        player_view = f'''{line2[avatar.pos_x - 1]}{line2[avatar.pos_x]}{line2[avatar.pos_x + 1]}
{line3[avatar.pos_x - 1]}◉{line3[avatar.pos_x + 1]}
{line4[avatar.pos_x - 1]}{line4[avatar.pos_x]}{line4[avatar.pos_x + 1]}'''
    if avatar.pos_y == 4:
        player_view = f'''{line3[avatar.pos_x - 1]}{line3[avatar.pos_x]}{line3[avatar.pos_x + 1]}
{line4[avatar.pos_x - 1]}◉{line4[avatar.pos_x + 1]}
{line5[avatar.pos_x - 1]}{line5[avatar.pos_x]}{line5[avatar.pos_x + 1]}'''
    if avatar.pos_y == 5:
        player_view = f'''{line4[avatar.pos_x - 1]}{line4[avatar.pos_x]}{line4[avatar.pos_x + 1]}
{line5[avatar.pos_x - 1]}◉{line5[avatar.pos_x + 1]}
{line6[avatar.pos_x - 1]}{line6[avatar.pos_x]}{line6[avatar.pos_x + 1]}'''
    if avatar.pos_y == 6:
        player_view = f'''{line5[avatar.pos_x - 1]}{line5[avatar.pos_x]}{line5[avatar.pos_x + 1]}
{line6[avatar.pos_x - 1]}◉{line6[avatar.pos_x + 1]}
{line7[avatar.pos_x - 1]}{line7[avatar.pos_x]}{line7[avatar.pos_x + 1]}'''
    if avatar.pos_y == 7:
        player_view = f'''{line6[avatar.pos_x - 1]}{line6[avatar.pos_x]}{line6[avatar.pos_x + 1]}
{line7[avatar.pos_x - 1]}◉{line7[avatar.pos_x + 1]}
{line8[avatar.pos_x - 1]}{line8[avatar.pos_x]}{line8[avatar.pos_x + 1]}'''
    if avatar.pos_y == 8:
        player_view = f'''{line7[avatar.pos_x - 1]}{line7[avatar.pos_x]}{line7[avatar.pos_x + 1]}
{line8[avatar.pos_x - 1]}◉{line8[avatar.pos_x + 1]}
{line9[avatar.pos_x - 1]}{line9[avatar.pos_x]}{line9[avatar.pos_x + 1]}'''
    if avatar.pos_y == 9:
        player_view = f'''{line8[avatar.pos_x - 1]}{line8[avatar.pos_x]}{line8[avatar.pos_x + 1]}
{line9[avatar.pos_x - 1]}◉{line9[avatar.pos_x + 1]}
{line10[avatar.pos_x - 1]}{line10[avatar.pos_x]}{line10[avatar.pos_x + 1]}'''
    if avatar.victory:
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
button = tk.Button(root, text="▲", command=lambda: move(0, -1), width=3, height=2)
button.grid(row=0, column=1)
# Ajout d'un widget Bouton à la fenêtre, qui appelle la fonction go_down lorsqu'il est pressé
button = tk.Button(root, text="▼", command=lambda: move(0, 1), width=3, height=2)
button.grid(row=2, column=1)
# Ajout d'un widget Bouton à la fenêtre, qui appelle la fonction go_left lorsqu'il est pressé
button = tk.Button(root, text="◀", command=lambda: move(-1, 0), width=2, height=3)
button.grid(row=1, column=0)
# Ajout d'un widget Bouton à la fenêtre, qui appelle la fonction go_right lorsqu'il est pressé
button = tk.Button(root, text="▶", command=lambda: move(1, 0), width=2, height=3)
button.grid(row=1, column=2)


# Définition de la taille et de la position de la fenêtre
# geometry("largeur x hauteur+x+y")
root.geometry("100x175+100+50")

# Boucle principale pour afficher la fenêtre
root.mainloop()
