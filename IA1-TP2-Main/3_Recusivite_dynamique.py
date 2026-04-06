import time


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

joueurs_tries = sorted(joueurs, key=lambda j: j["score"], reverse=True)

def score_cumule(liste, k):
    if k == 0:
        print(f"score_cumule(joueurs, {k}) = 0")
        return 0, ""

    prev_total, prev_score = score_cumule(liste, k-1)
    joueur = liste[k-1]
    score = joueur["score"]

    if prev_score:
        expression = f"{prev_score} + {score}"
    else:
        expression = f"{score}"

    print(f"score_cumule(joueurs, {k}) = 0 + {expression}  ({joueur['nom']})  = {prev_total + score}")
    total = prev_total + score
    return total, expression

# fibonacci
# fib(0) = 93
# fib(1) = 91
# fib(n) = fib(n-1) + fib(n-2)
nums = [93, 91]

def fib_naif(n):
    if n == 0:
        return nums[0]
    if n == 1:
        return nums[1]
    resultat = fib_naif(n-1) + fib_naif(n-2)
    return resultat



def fib_memo(n, memo={}):
    if n == 0:
        return nums[0]
    if n == 1:
        return nums[1]
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]





if __name__ == "__main__":
    total, expression = score_cumule(joueurs_tries, 2)

    n= 35
    # debut = time.perf_counter()
    # resultat = fib_naif(n)
    # fin = time.perf_counter()
    # print(f"fib_naif({n}) = {resultat} Temps : { fin - debut: .3f} s")


    debut = time.perf_counter()
    resultat = fib_memo(n)
    fin = time.perf_counter()
    print(f"fib_memo({n}) = { resultat} Temps : { fin - debut: .6f} s")
