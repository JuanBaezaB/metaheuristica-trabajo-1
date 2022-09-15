import numpy as np
import random

def Diagonalcollisions(a):
    i = 0
    j = 0
    count = 0
    while i<len(a)-1:
        while j<len(a)-1:
            if abs(a[i]-a[j]) < abs(i-j):
                count += 1
                print(str(a[i]) + " " + str(a[j]) + " " + str(i) + " " + str(j))
            j += 1
        i += 1
        j = 0
    return count

def fitness(a, b):
    return a+b

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
b = Diagonalcollisions(table)
print(b)



