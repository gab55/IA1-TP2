import matplotlib.pyplot as plt
import importlib
module = importlib.import_module("3_Recusivite_dynamique")
call_fib_memo = module.call_fib_memo
call_fib_naif = module.call_fib_naif

def tableau_2():
    naif = {}
    memo = {}
    for i in range(1,25):
        resultat_naif, calls_naif = call_fib_naif(i)
        naif[i] = [resultat_naif, calls_naif]
        resultat_memo, calls_memo = call_fib_memo(i)
        memo[i] = [resultat_memo, calls_memo]
    # print(naif)
    # print(memo)
    liste_call_naif = [values[1] for values in naif.values()]
    liste_call_memo = [values[1] for values in memo.values()]
    plt.plot(list(naif.keys()), liste_call_naif, label="naif")
    plt.plot(list(memo.keys()), liste_call_memo, label="memo")
    plt.yscale("log")
    plt.title("Croissance du nombre d’appels récursifs", fontsize=14)
    plt.ylabel("No. d'appels rercursifs")
    plt.xlabel("n values")
    plt.legend()
    plt.grid(axis='y', linestyle=':', alpha=0.7)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    tableau_2()