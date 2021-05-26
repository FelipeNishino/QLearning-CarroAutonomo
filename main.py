from QLearn import QLearn
from Constants import *

print("Digite o valor de alfa: (default = 0.2)")
alfa = float(input() or 0.2)
print()

print("Digite o valor de gama: (default = 0.8)")
gama = float(input() or 0.8)
print()

print("Digite o valor de epsilon: (default = 0.9)")
epsilon = float(input() or 0.9)
print()

print("Digite o valor do decaimento de epsilon: (default = 0.5)")
epsilonDecay = float(input() or 0.5)
print()

print("Digite o valor mínimo do epsilon: (default = 0.2)")
epsilonMin = float(input() or 0.2)
print()

print("Digite a quantidade de gerações: (default = 1000)")
maxGen = int(input() or 1000)
print()

print("Digite as coordenadas do carro de vanessa: (Usar o formato \"x,y\" na base 0)")
initialPosition = [int(coord) for coord in (input() or "4,6").split(",")]
print()

print("Digite as coordenadas da vanessa: (Usar o formato \"x,y\" na base 0)")
target = [int(coord) for coord in (input() or "9,5").split(",")]
print()

environment[target[0]][target[1]] = t

a = QLearn(alfa, gama, epsilon, epsilonDecay, epsilonMin, rewards, environment)
print("Treinando...")
print()
a.train(maxGen)
print()
print("Executando...")
print()
a.exec(initialPosition[0], initialPosition[1])

# (0,0), (4,6)
# (5,2), (1,8)