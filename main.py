import json, os, random
from random import sample

class Table:
    def __init__(self, couleur, numero):
        self.couleur = couleur
        self.numero = numero

    def __repr__(self):
        return f"[{self.couleur}, {self.numero}]"

class Main:
    def __init__(self, main, pseudo):
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

    def cartes_posables(self, main, table):
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

        main_actuel1 = sample(total_cartes, k=7)

        main_actuel2 = sample(total_cartes, k=7)

        print("Bienvenue au Uno")
        pseudo1 = input("Choix pseudo 1 : ")
        clear()
        print("Bienvenue au Uno")
        pseudo2 = input("Choix pseudo 2 : ")
        clear()
        print(f"{pseudo1}, voici vos cartes :")
        print(main_actuel1)
        input("Appuyer sur entré pour continuer")
        clear()
        print(f"{pseudo2}, voici vos cartes")
        print(main_actuel2)
        input("Appuyer sur entré pour continuer")

        self.J1 = Main(main_actuel1, pseudo1)
        self.J2 = Main(main_actuel2, pseudo2)

    
    def run(self):
        while len(self.J1.main) > 0 and len(self.J2.main) > 0:
            clear()

            ##### Tour J1 #####
            print(f"Table : {self.table} \n")
            print(f"{self.J1.pseudo}, c'est à vous de jouer. Voici vos cartes :")
            print(self.J1.main)
            self.J1.choix([self.table.couleur, self.table.numero])
            self.table.couleur = self.J1.table_actu[0]
            self.table.numero = self.J1.table_actu[1]
            input("Taper Entrée pour passer au joueur suviant...")
            clear()

            ##### Tour J2 #####
            print(f"Table : {self.table} \n")
            print(f"{self.J2.pseudo}, c'est à vous de jouer. Voici vos cartes :")
            print(self.J2.main)
            self.J2.choix([self.table.couleur, self.table.numero])
            self.table.couleur = self.J2.table_actu[0]
            self.table.numero = self.J2.table_actu[1]
            input("Taper Entrée pour passer au joueur suviant...")
        
        clear()
        if len(self.J1.main) == 0:
            print(f"Bravo {self.J1.pseudo}, vous avez gagner !")
        elif len(self.J2.main) == 0:
            print(f"Bravo {self.J2.pseudo}, vous avez gagner !")
        else:
            print("Bug :(")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

with open('data.json', 'r', encoding='utf-8') as f:
    total_cartes = json.load(f)

Partie_en_cour = Jeu()
Partie_en_cour.run()
