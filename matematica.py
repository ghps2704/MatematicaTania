import numpy as np

matriz3x2 = [[100, 50], [50, 100], [50, 50]]
matriz2x3 = [[3, 1, 3]], [6, 5, 5]

matrizmult = np.dot(matriz2x3, matriz3x2)
resultjunho = matrizmult[1][1] + matrizmult [0][1]
resultmaio = matrizmult [0][0] + matrizmult[1][0]

print("== Junho Maio==")
print(matrizmult)
print("------------------------------------")
print("O total de botões em Junho será de {}".format(resultjunho))
print("O total de botões em Maio será de {}".format(resultmaio))
print("------------------------------------")