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


def lepoids(equipe, joueur):
    poids_actuel = sum(j['poids'] for j in equipe)
    return poids_actuel + joueur['poids']


def lebudget(equipe_a, equipe_b, nouveau_joueur):
    depenses = sum(j['salaire'] for j in equipe_a) + sum(j['salaire'] for j in equipe_b)
    return depenses + nouveau_joueur['salaire']


def lesscores(liste_joueurs):
    joueurs_tries = sorted(liste_joueurs, key=lambda j: j["score"], reverse=True)  # jai utiliser le trie ici

    equipe_A = []
    equipe_B = []

    def backtrack(index):
        nonlocal equipe_A, equipe_B

        if len(equipe_A) == 3 and len(equipe_B) == 3:
            return True

        if index >= len(joueurs_tries):
            return False

        j = joueurs_tries[index]

        if len(equipe_A) < 3 and (j not in equipe_A) and (j not in equipe_B):
            if lepoids(equipe_A, j) <= POIDS and lebudget(equipe_A, equipe_B, j) <= BUDGET:
                equipe_A.append(j)
                if backtrack(index + 1):
                    return True
                equipe_A.pop()

        if len(equipe_B) < 3 and (j not in equipe_A) and (j not in equipe_B):
            if lepoids(equipe_B, j) <= POIDS and lebudget(equipe_A, equipe_B, j) <= BUDGET:
                equipe_B.append(j)
                if backtrack(index + 1):
                    return True
                equipe_B.pop()
        if backtrack(index + 1):
            return True
        return False

    if backtrack(0):
        return equipe_A, equipe_B
    else:
        print("Impossible de former les equipes")
        return equipe_A, equipe_B


if __name__ == "__main__":
    a, b = lesscores(joueurs)
    print(f"score total: {sum(j['score'] for j in a) + sum(j['score'] for j in b)}")  # pour aider avec tableau
    print(f"budget total: {sum(j['salaire'] for j in a) + sum(j['salaire'] for j in b)}")  # pour aider avec tableau

    print(f"Équipe A: {[j['nom'] for j in a]} (Score: {sum(j['score'] for j in a)})")
    print(f"Équipe B: {[j['nom'] for j in b]} (Score: {sum(j['score'] for j in b)})")

