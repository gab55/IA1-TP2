joueurs = [
    {"nom": "Alice", "score": 88, "salaire": 1200, "poids": 72},
    {"nom": "Bob", "score": 91, "salaire": 1800, "poids": 85},
    {"nom": "Clara", "score": 84, "salaire": 950, "poids": 68},
    {"nom": "David", "score": 93, "salaire": 2100, "poids": 90},
    {"nom": "Emma", "score": 79, "salaire": 800, "poids": 65},
    {"nom": "Frank", "score": 87, "salaire": 2400, "poids": 95},
    {"nom": "Grace", "score": 85, "salaire": 1050, "poids": 70},
    {"nom": "Hugo", "score": 89, "salaire": 1600, "poids": 80},
]

BUDGET = 8500 
POIDS = 250

def lepoids(equipe, nouveau_joueur):
    poids_total = sum(j['poids'] for j in equipe)
    return (poids_total + nouveau_joueur['poids'])

def lebudget(equipe_a, equipe_b, nouveau_joueur):
    depenses = sum(j['salaire'] for j in equipe_a) + sum(j['salaire'] for j in equipe_b)
    return (depenses + nouveau_joueur['salaire'])

def strategie_alternance(liste_joueurs):
    disponibles = liste_joueurs.copy()
    equipe_A = []
    equipe_B = []
    count = 0

    while (len(equipe_A) < 3 or len(equipe_B) < 3) and disponibles:
        
        equipe_actuelle = equipe_A if len(equipe_A) < 3 else equipe_B

        if count % 2 == 0: #jai utiliser le tri ici
            joueurs_tries = sorted(disponibles, key=lambda j: j["score"], reverse=True)
        else:
            joueurs_tries = sorted(disponibles, key=lambda j: j["score"] / j["salaire"], reverse=True)

        joueur_trouve = False
        for j in joueurs_tries:
            if lepoids(equipe_actuelle, j) <= POIDS and lebudget(equipe_A, equipe_B, j) <= BUDGET:
                equipe_actuelle.append(j)
                disponibles.remove(j)
                count += 1            
                joueur_trouve = True
                break
        
        if not joueur_trouve:
            break

    if len(equipe_A) < 3 or len(equipe_B) < 3:
        print(" Impossible")
        print(f"Budget ({sum(j['salaire'] for j in equipe_A+equipe_B)}$) ou Poids atteint.")
    
    return equipe_A, equipe_B

if __name__ == "__main__":
    team_a, team_b = strategie_alternance(joueurs)
    
    print(f"Équipe A: {[j['nom'] for j in team_a]} (Score total: {sum(j['score'] for j in team_a)})")
    print(f"Équipe B: {[j['nom'] for j in team_b]} (Score total: {sum(j['score'] for j in team_b)})")