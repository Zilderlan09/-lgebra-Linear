import numpy as np
from matplotlib import pyplot as plt

# Função de ajuste (hipotética, a ser confirmada)
def fit_f(i, B, L):
    return i * L * B

# Coleta dos dados
i = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5])
L_1 = 0.0125
L_2 = 0.025
L_3 = 0.05
L_4 = 0.1
f_l1 = np.array([31.5, 31.55, 31.63, 31.7, 31.74, 31.82, 31.9, 31.94, 32, 32.04])
f_l2 = np.array([30.65, 30.8, 30.92, 31.03, 31.15, 31.25, 31.36, 31.5, 31.63, 31.73])
f_l3 = np.array([37.86, 38.1, 38.31, 38.53, 38.72, 38.94, 39.15, 39.4, 39.62, 39.71])
f_l4 = np.array([40.31, 40.75, 41.15, 41.5, 41.97, 42.42, 42.83, 43.22, 43.64, 44.04])

# Exibindo gráficos
plt.scatter(i, f_l1, color='r', label="L_1")
plt.scatter(i, f_l2, color='g', label="L_2")
plt.scatter(i, f_l3, color='b', label="L_3")
plt.scatter(i, f_l4, color='k', label="L_4")
plt.legend(loc="upper left")
plt.xlabel("Corrente")
plt.ylabel("Força Magnética")
plt.show()

# Processamento dos dados
f_l1_novo = (f_l1 - f_l1[0]) * 9.8
f_l2_novo = (f_l2 - f_l2[0]) * 9.8
f_l3_novo = (f_l3 - f_l3[0]) * 9.8
f_l4_novo = (f_l4 - f_l4[0]) * 9.8

# Gráficos com dados tratados
plt.scatter(i, f_l1_novo, color='r', label="L_1")
plt.scatter(i, f_l2_novo, color='g', label="L_2")
plt.scatter(i, f_l3_novo, color='b', label="L_3")
plt.scatter(i, f_l4_novo, color='k', label="L_4")
plt.legend(loc="upper left")
plt.xlabel("Corrente")
plt.ylabel("Força Magnética (Tratada)")
plt.show()

# Função de ajuste para mínimos quadrados
def fit_f(i, B, L):
    return i * L * B

# Ajuste por mínimos quadrados para determinar B
def ajuste_minimos_quadrados(i, f_obs, L):
    # B é calculado com base nos mínimos quadrados
    B = np.sum(i * f_obs) / np.sum(i**2 * L)
    return B

# Aplicando ajuste de mínimos quadrados para cada conjunto
B_1 = ajuste_minimos_quadrados(i, f_l1_novo, L_1)
B_2 = ajuste_minimos_quadrados(i, f_l2_novo, L_2)
B_3 = ajuste_minimos_quadrados(i, f_l3_novo, L_3)
B_4 = ajuste_minimos_quadrados(i, f_l4_novo, L_4)

# Exibindo gráficos com observados e ajustados
plt.scatter(i, f_l1_novo, color='r', label="L_1 (obs)")
plt.plot(i, fit_f(i, B_1, L_1), color='r', label="L_1 (ajustado)")
plt.scatter(i, f_l2_novo, color='g', label="L_2 (obs)")
plt.plot(i, fit_f(i, B_2, L_2), color='g', label="L_2 (ajustado)")
plt.scatter(i, f_l3_novo, color='b', label="L_3 (obs)")
plt.plot(i, fit_f(i, B_3, L_3), color='b', label="L_3 (ajustado)")
plt.scatter(i, f_l4_novo, color='k', label="L_4 (obs)")
plt.plot(i, fit_f(i, B_4, L_4), color='k', label="L_4 (ajustado)")

plt.legend(loc="upper left")
plt.xlabel("Corrente")
plt.ylabel("Força Magnética (Tratada)")
plt.show()
