import math

from tabulate import tabulate
import importlib
module_algo_glu = importlib.import_module("2_algo_glouton_backtrack")
module_glu_score_salaire = importlib.import_module("2b_glouton")
module_glu_score_ratio = importlib.import_module("2d_glouton")


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

joueurs_optimal = {
    "A" : [
        {"nom": "Clara", "score": 84, "salaire": 950, "poids": 68},
        {"nom": "Emma", "score": 79, "salaire": 800, "poids": 65},
        {"nom": "Hugo", "score": 89, "salaire": 1600, "poids": 80},
    ],
    "B" : [
        {"nom": "Alice", "score": 88, "salaire": 1200, "poids": 72},
        {"nom": "Bob", "score": 91, "salaire": 1800, "poids": 85},
        {"nom": "David", "score": 93, "salaire": 2100, "poids": 90},
    ],
}

def form_equipe(module_algo):
    team_roster = {"A": [], "B": []}
    team_a, team_b = module_algo(joueurs)
    for i in team_a:
        team_roster["A"].append(i)
    for i in team_b:
        team_roster["B"].append(i)
        # print(team_roster["A"])
        # print(team_roster["B"])
    team_roster["A"].sort(key=lambda x: x["score"], reverse=True)
    team_roster["B"].sort(key=lambda x: x["score"], reverse=True)
    # print(team_roster["A"])
    # print(team_roster["B"])
    return team_roster

joueurs_glouton = form_equipe(module_algo_glu.lesscores)
joueurs_score_salaire = form_equipe(module_glu_score_salaire.lesratios)
joueurs_score_ratio = form_equipe(module_glu_score_ratio.strategie_alternance)





def total_equipe(equipe):
    score_total = 0
    poids_total = 0
    salaire_total = 0
    for team, joueurs_equipe in equipe.items():
        for joueur in joueurs_equipe:
            score_total += joueur["score"]
            poids_total += joueur["poids"]
            salaire_total += joueur["salaire"]

    return score_total, poids_total, salaire_total



score_pulp, _, budget_pulp  = total_equipe(joueurs_optimal)
score_glouton, _, budget_glouton = total_equipe(joueurs_glouton)
score_salaire, _, budget_salaire = total_equipe(joueurs_score_salaire)
score_ratio, _, budget_ratio = total_equipe(joueurs_score_ratio)


methodes = [
    {"score": score_pulp, "budget": budget_pulp, "methode": "PuLP (optimal)"},
    {"score": score_glouton, "budget": budget_glouton, "methode": "Glouton"},
    {"score": score_salaire, "budget": budget_salaire, "methode": "Salaire"},
    {"score": score_ratio, "budget": budget_ratio, "methode": "Ratio"},
]

methodes.sort(key=lambda x: ( +1 if x["methode"] == "PuLP" else 0, x["score"]), reverse=True)




headers = ["      ", "Score Total", "Budget Utilisé", "Écart vs optimal"]
data = []

for methode in methodes:
        data.append([ methode["methode"], methode["score"], methode["budget"], f"{(methode['score']- score_pulp)} pts. {(methode['score']- score_pulp)/score_pulp*100:.2f}"])


table = tabulate(data, headers=headers, tablefmt="plain", colalign=("left", "right", "right", "right"))


table_lines = table.split("\n")
table_width = max(len(line) for line in table_lines)
title = "Tableau Comparatif"
title = title.center(table_width)
table = f"{title}\n{table}"
print(table)
with open("plt/tableau_comparitif.txt", "w") as f:
    f.write(table)
