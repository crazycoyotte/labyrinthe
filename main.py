# Import
import tkinter as tk
import player
import labyrinthe

# instanciation du joueur
avatar = player.Player()

# instanciation du labyrinthe
laby = labyrinthe.Labyrinthe()

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
    avatar.move2(x, y, laby)
    update_label()


def view():
    player_view = ""
    #player_line = laby.structure[avatar.pos_y]
    cam_y = -2
    cam_x = -2
    for i in range(avatar.pos_y - 1, avatar.pos_y + 2, 1):
        player_line = laby.structure[i]
        cam_y += 1
        cam_x = -2
        for j in range(avatar.pos_x - 1, avatar.pos_x + 2, 1):
            cam_x += 1
            print(f"cam_x : {cam_x} / cam_y : {cam_y}")
            if cam_x == 0 and cam_y == 0:
                player_view += "☺"
            else:
                player_view += player_line[j]
        player_view += "\n"
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
