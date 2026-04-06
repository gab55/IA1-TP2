from utils import get_dataset
from pulp import *



prob = LpProblem("Deux_Equipes", LpMaximize)

groups = ["A", "B"]
salaireMax = 8500
poidsMax = 250

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

noms = [joueur["nom"] for joueur in joueurs]



variables = LpVariable.dicts("x", (noms, groups), cat="Binary")
print(f"variables : {variables}")

prob += (
    lpSum([variables[joueur["nom"]][g] * joueur["score"]
           for joueur in joueurs
           for g in groups]), "scoreTotal"
    )

# Contraintes
# 3 joueurs par equipe
for g in groups:
    prob += (lpSum(variables[nom][g] for nom in noms) == 3, f"nbJoueurEquipe-{g}")

# seulement 1 equpe par joueur max
for nom in noms:
    prob += (lpSum(variables[nom][g] for g in groups) <= 1, f"max1Equipe-{nom}")

# 6000$ max budget
prob += (lpSum(
        variables[joueur["nom"]][g] * joueur["salaire"]
           for joueur in joueurs
            for g in groups
) <= salaireMax, f"SalaireTotal")



# 250kg max par equipe
for g in groups:
    prob += (
    lpSum([variables[joueur["nom"]][g] * joueur["poids"]
           for joueur in joueurs
           ]) <= 250, f"PoidsTotal-{g}"
    )


# resudre le probleme
prob.writeLP("prog_linear.lp")
prob.solve()
print("statut : \n\t", LpStatus[prob.status])




# afficher le resultats

def team_total(team):

    score = sum(joueur["score"]* variables[joueur["nom"]][team].varValue for joueur in joueurs)
    salaire = sum(joueur["salaire"]* variables[joueur["nom"]][team].varValue for joueur in joueurs)
    return score , salaire

def team_delta(team):
    other_team = None
    if team in groups:
        if team == groups[0]:
            other_team = groups[1]
        elif team == groups[1]:
            other_team = groups[0]

        team_score, team_salaire = team_total(team)
        other_team_score, other_team_salaire = team_total(other_team)

        delta_score = team_score - other_team_score
        delta_salaire = team_salaire - other_team_salaire
        pc_score =  100 * team_score / (team_score + other_team_score)
        pc_salaire = 100 * team_salaire / (team_salaire + other_team_salaire)
        return delta_score, delta_salaire, pc_score, pc_salaire

    else:
        print("Error team_delta() : team must be in groups")
        return None


def afficher_equipe(team):
    print("\n", end="")
    if team == "A":
        print(f"\t\tScore Equipe : {team_total('A')[0]} points -- Δ: {team_delta('A')[0]:.0f}points  {team_delta('A')[2]:.1f}%")
        print(f"\t\tSalaire Equipe : {team_total('A')[1]:.0f}$ -- Δ: {team_delta('A')[1]:.0f}$  {team_delta('A')[3]:.1f}%")
        print(f"\t\tPoids Total A : {(poidsMax + prob.constraints['PoidsTotal_A'].value()):.0f}kg sur {poidsMax}kg -- "
              f"Δ: {prob.constraints['PoidsTotal_A'].value():.0f} kg  {(100 * (poidsMax + prob.constraints['PoidsTotal_A'].value()) / poidsMax):.1f}%")

    if team == "B":
        print(f"\t\tScore Equipe : {team_total('B')[0]} points -- Δ: {team_delta('B')[0]:.0f}points  {team_delta('B')[2]:.1f}%")
        print(f"\t\tSalaire Equipe : {team_total('B')[1]:.0f}$ -- Δ: {team_delta('B')[1]:.0f}$  {team_delta('B')[3]:.1f}%")
        print(f"\t\tPoids Total B : {(poidsMax + prob.constraints['PoidsTotal_B'].value()):.0f}kg sur {poidsMax}kg -- "
              f"Δ: {prob.constraints['PoidsTotal_B'].value():.0f}kg  {(100 * (poidsMax + prob.constraints['PoidsTotal_B'].value()) / poidsMax):.1f}%")


def afficher_solution():
    print("solution : ")
    print("\tMax Score:", prob.objective.value(), "points")
    print("Constraints:")
    salaire_ut = int(salaireMax + prob.constraints['SalaireTotal'].value())
    print(f"\tsalaire total: {salaire_ut}$ sur {salaireMax}$ -- Δ: {salaire_ut/salaireMax*100:.0f}% , {prob.constraints['SalaireTotal'].value():.0f}$")


    for g in groups:
        print(f"\tEquipe {g}")
        print("\t\tJoueurs : ", end=" ")

        for nom in noms:
            if variables[nom][g].varValue == 1.0:

                print(nom, end="  ")
        afficher_equipe(f"{g}")

afficher_solution()