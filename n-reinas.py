import numpy as np
import random


seed, tamaño_tabl, tamaño_pobl, prob_cruza, prob_mut, num_ite  = map(int, input("Ingresa 6 valores: ").split())

print("seed: ", seed)
print("tamaño_tabl: ", tamaño_tabl)
print("tamaño_pobl : ", tamaño_pobl)
print("prob_cruza : ", prob_cruza)
print("prob_mut : ", prob_mut)
print("num_ite : ", num_ite)

random.seed(seed)

table = np.array([i for i in range(1, tamaño_tabl+1)])
print(table)

random.shuffle(table)

print(table)



