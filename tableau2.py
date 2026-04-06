import matplotlib.pyplot as plt
import numpy as np

equipe_A = [0.52, 0.335, 0.21]
equipe_B = [0.72, 0.51, 0.24]

categories = ['Score', 'Salaire', 'Poids']
x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

rects1 = ax.bar(x - width/2, equipe_A, width, label='Équipe A', color='skyblue')
rects2 = ax.bar(x + width/2, equipe_B, width, label='Équipe B', color='salmon')

ax.set_ylabel('Valeur de 0 a 1')
ax.set_title('Comparaison équipes')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_ylim(0, 1.1)
ax.legend()

plt.show()