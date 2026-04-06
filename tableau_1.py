import matplotlib.pyplot as plt

def score_total():
    scores = {
        "Meilleur ratio score / salaire": 516,
        "Alternance score / ratio": 521,
        "PuLP": 524
    }

    couleurs = ['steelblue', 'salmon', 'green']

    plt.figure(figsize=(8, 6))

    for i, (nom, score) in enumerate(scores.items()):
        plt.bar(nom, score, color=couleurs[i], label=f"{nom} ({score})")

    score_optimal = scores["PuLP"]
    plt.axhline(y=score_optimal, color='red', linestyle='--', alpha=0.6, label=f"Optimal: {score_optimal}")

    plt.title("Comparaison de perfomance", fontsize=14)
    plt.ylabel("Score Total")
    plt.ylim(500, 530)
    plt.legend()
    plt.grid(axis='y', linestyle=':', alpha=0.7)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    score_total()