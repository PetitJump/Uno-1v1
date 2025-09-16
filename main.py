import json, os
from random import sample

class Jeu:
    def __init__(self):
        clear()
        self.table = sample(total_cartes, k=1)[0]
        self.table = Table(self.table[0][0], self.table[0][1] )
        print("Bienvenue au Uno")
        self.pseudo1 = input("Choix pseudo 1 : ")
        clear()
        print("Bienvenue au Uno")
        self.pseudo2 = input("Choix pseudo 2 : ")
        clear()
        print(f"{self.pseudo1}, voici vos cartes :")
        self.main_actuel1 = sample(total_cartes, k=7)
        print(self.main_actuel1)
        input("Appuyer sur entré pour continuer")
        clear()
        print(f"{self.pseudo2}, voici vos cartes")
        self.main_actuel2 = sample(total_cartes, k=7)
        print(self.main_actuel2)
        input("Appuyer sur entré pour continuer")

    def cartes_posables(self, main):
        rendu = []
        for c in main:
            if c[0] == self.table[0] or c[1] == self.table[1]:
                rendu.append(c)
        return rendu
    
    def run(self):
        while len(self.main_actuel1) > 0 and len(self.main_actuel2) > 0:
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
Partie_en_cour.run()
