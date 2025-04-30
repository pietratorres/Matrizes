dados = [0.90, 1.42, 1.30, 1.55, 1.63, 1.32, 1.35, 1.47, 1.95, 1.66, 1.96, 1.47, 1.92, 1.35, 1.05, 1.85, 1.74, 1.65, 1.78, 1.71, 2.29, 1.82, 2.06, 2.14, 1.27]

import seaborn as sns
import matplotlib.pyplot as plt

hist =  sns.histplot(dados, kde=True, binwidth=0.2, binrange=(0.8, 2.4))
plt.show()