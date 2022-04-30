from matplotlib import pyplot as plt

# Sprint 1:
S1eixoX = [0, 1, 2, 3, 4, 5]
# eixoY = tarefas a serem feitas - tarefas feitas realmente:
S1eixoY = [4.25, 4.25-(1/3), 4.25-(2/3), 4.25-1, 4.25-1.25, 4.25-3.5]

# Y = tarefas a serem feitas - tarefas a serem feitas de acordo com  a previsão (linearmente):
X = [0, 1, 2, 3, 4, 5]
Y = [5*0.85, 4*0.85, 3*0.85, 2*0.85, 1*0.85, 0]

# Sprint 2:
S2eixoX = [0, 1, 2, 3]
# eixoY = tarefas a serem feitas - tarefas feitas realmente:
S2eixoY = [4.75, 4.75-0.5, 4.75-1, 4.75-2.25]

# Y = tarefas a serem feitas - tarefas a serem feitas de acordo com  a previsão (linearmente):
X = [0, 1, 2, 3, 4, 5]
Y = [5*0.95, 4*0.95, 3*0.95, 2*0.95, 1*0.95, 0]

# Gráfico SPI e CPI:
BAC = 500600
#PV = BAC * P%C
#EV = BAC * A%C
#SPI = EV/PV = EV/(BAC*P%C)
#CPI = EV/AC = EV/(BAC*A%C)

SPIeixoX = [1, 2, 3, 4, 5, 6, 7, 8]
SPIeixoY = [0.8, 0.7, 0.53, 0.75, 0.96, 0.9, 0.84, 0.78]
CPIeixoX = [1, 2, 3, 4, 5, 6, 7, 8]
CPIeixoY = [1.07, 1.11, 1.13, 0.95, 0.96, 0.94, 0.96, 0.91]

plt.plot(SPIeixoX, SPIeixoY, "-b", label="SPI")
plt.scatter(SPIeixoX, SPIeixoY, marker='o');
plt.plot(CPIeixoX, CPIeixoY, "-r", label="CPI")
plt.scatter(CPIeixoX, CPIeixoY, marker='o');
plt.legend(loc="lower right")
plt.show()