from matplotlib import pyplot as plt

# Sprint 1:
S1eixoX = [0, 1, 2, 3, 4, 5]
# eixoY = tarefas a serem feitas - tarefas feitas realmente:
S1eixoY = [4.25, 4.25-(1/3), 4.25-(2/3), 4.25-1, 4.25-1.25, 4.25-3.5]

# Y = tarefas a serem feitas - tarefas a serem feitas de acordo com  a previsão (linearmente):
X = [0, 1, 2, 3, 4, 5]
Y = [5*0.85, 4*0.85, 3*0.85, 2*0.85, 1*0.85, 0]

plt.plot(X, Y)
plt.plot(S1eixoX, S1eixoY)
plt.show()

# Sprint 2:
S2eixoX = [0, 1, 2, 3]
# eixoY = tarefas a serem feitas - tarefas feitas realmente:
S2eixoY = [4.75, 4.75-0.5, 4.75-1, 4.75-2.25]

# Y = tarefas a serem feitas - tarefas a serem feitas de acordo com  a previsão (linearmente):
X = [0, 1, 2, 3, 4, 5]
Y = [5*0.95, 4*0.95, 3*0.95, 2*0.95, 1*0.95, 0]

plt.plot(X, Y)
plt.plot(S2eixoX, S2eixoY)
plt.show()

# Gráfico SPI e CPI:
BAC = 500600
#PV = BAC * P%C
#EV = BAC * A%C
#SPI = EV/PV = EV/(BAC*P%C)
#CPI = EV/AC = EV/(BAC*A%C)

SPIeixoX = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
SPIeixoY = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
CPIeixoX = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
CPIeixoY = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]