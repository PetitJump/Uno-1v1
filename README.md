# Uno 1v1

Un petit jeu de Uno en Python, en duel (1 contre 1).  
Chaque joueur commence avec 7 cartes, et le but est d’être le premier à poser toutes ses cartes.

---

## 📖 Règles du jeu

- Le jeu charge les cartes depuis `data.json` (nombres de 1 à 9 dans 4 couleurs : bleu, rouge, vert, jaune).  
- L'utilisateur choisit combien de joueurs vont jouer.
- Chaque joueur reçoit 7 cartes aléatoires.  
- Une carte de départ est placée sur la table.  
- À son tour, le joueur peut poser une carte de la même couleur ou du même numéro que celle de la table.  
- S’il ne peut pas jouer, il pioche une carte.  
- Le premier à ne plus avoir de cartes gagne la partie !  

---

## 🛠 Améliorations possibles

- Ajouter les cartes spéciales (+2, +4, passe ton tour… ).  
- Faire une pile recyclable (éviter les doublons de cartes).