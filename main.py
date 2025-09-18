import json, os, random
from random import sample

class Table:
    def __init__(self, couleur: str, numero: int):
        self.couleur = couleur
        self.numero = numero

    def __repr__(self):
        return f"[{self.couleur}, {self.numero}]"

class Main:
    def __init__(self, main: list, pseudo: str):
        self.main = main
        self.pseudo = pseudo
        self.table_actu = ["couleur", 0]

    def choix(self, table: list[str, int]):
        carte_dispo = self.cartes_posables(self.main, table) #carte_dispo = list
        print("")
        if len(carte_dispo) > 0:
            print("Voici les cartes que vous pouvez jouer :")
            for i in range(len(carte_dispo)):
                print(f"{i + 1} : {carte_dispo[i]}")
            choix = int(input("Votre choix : "))
            carte_jouer = carte_dispo[choix - 1]
            self.main.remove(carte_jouer)
            self.table_actu = carte_jouer
        else:
            self.table_actu = table
            print("Vous n'avez pas la possibilité de jouer une carte")
            print("Vous piochez donc une carte.")
            nouvelle_carte = random.choice(total_cartes)
            print(f"Carte piocher : {nouvelle_carte}")
            self.main.append(nouvelle_carte) 

    def cartes_posables(self, main: list, table: list):
        rendu = []
        for c in main:
            if c[0] == table[0] or c[1] == table[1]:
                rendu.append(c)
        return rendu

class Jeu:
    def __init__(self):
        clear()
        self.table = sample(total_cartes, k=1)[0]
        self.table = Table(self.table[0], self.table[1] )

        total_joueur = int(input("Combien de joueurs vont jouer ? : "))
        self.joueur = []
        for i in range(total_joueur):
            clear()
            pseudo = input(f"Pseudo {i+1} : ")
            self.joueur.append(Main(sample(total_cartes, k=7), pseudo))


        for k in self.joueur:
            print(f"{k.pseudo} voici vos cartes : \n{k.main}")
    
    def joueur_vivant(self):
        for k in self.joueur:
            if len(k.main) == 0:
                return False
        return True

    def run(self):
        while self.joueur_vivant() == True:
            for k in self.joueur:
                if len(k.main) == 0:
                    break
                clear()
                print(f"Table : {self.table} \n")
                print(f"{k.pseudo}, c'est à vous de jouer. Voici vos cartes :")
                print(k.main)
                k.choix([self.table.couleur, self.table.numero])
                self.table.couleur = k.table_actu[0]
                self.table.numero = k.table_actu[1]
                input("Taper Entrée pour passer au joueur suviant...")

        clear()
        for k in self.joueur:
            if len(k.main) == 0:
                print(f"Bravo {k.pseudo} vous avez gagner !")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear') #Cleat le terminal

with open('data.json', 'r', encoding='utf-8') as f:
    total_cartes = json.load(f)

Partie_en_cour = Jeu()
Partie_en_cour.run()