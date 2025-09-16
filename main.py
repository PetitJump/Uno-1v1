import json, os
from random import sample

class Jeu:
    def __init__(self, main1: list[list], main2: list[list], table: list[str, int]):
        self.main1 = main1
        self.main2 = main2
        self.table = table

    def debut(self):
        clear()
        table = sample(total_cartes, k=1)[0]
        self.table = Table(table[0][0], table[0][1] )
        print("Bienvenue au Uno")
        pseudo1 = input("Choix pseudo 1 : ")
        clear()
        print("Bienvenue au Uno")
        pseudo2 = input("Choix pseudo 2 : ")
        clear()
        print(f"{pseudo1}, voici vos cartes :")
        main_actuel1 = sample(total_cartes, k=7)
        print(main_actuel1)
        print(f"{pseudo2}, voici vos cartes")
        input("Appuyer sur entré pour continuer")
        clear()
        main_actuel2 = sample(total_cartes, k=7)
        print(main_actuel2)
        input("Appuyer sur entré pour continuer")
    
    def cartes_posables(self, main):
        rendu = []
        for c in main:
            if c[0] == self.table[0] or c[1] == self.table[1]:
                rendu.append(c)
        return rendu
    
    def run(self):
        while len(self.main1) > 0 and len(self.main2) > 0:
            print("")
        

class Table:
    def __init__(self, couleur, numero):
        self.couleur = couleur
        self.numero = numero
    def __repr__(self):
        return [self.couleur, self.numero]

class Main:
    def __init__(self):
        pass

def clear():
    """Efface le terminal (Windows ou Linux/Mac)"""
    os.system('cls' if os.name == 'nt' else 'clear')

with open('data.json', 'r', encoding='utf-8') as f:
    total_cartes = json.load(f)

Partie_en_cour = Jeu()
Partie_en_cour.debut()
