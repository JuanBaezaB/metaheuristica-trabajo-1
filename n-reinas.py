import numpy as np
import time
import sys

start = time.time()

def pobl_inicial(tamaño_tabl, tamaño_pobl):
    poblacion = np.zeros([tamaño_pobl, tamaño_tabl], dtype=int)
    for k in range(tamaño_pobl):
        poblacion[k] = np.arange(0,tamaño_tabl)
        np.random.shuffle(poblacion[k])
    return poblacion

if len(sys.argv) == 7:
    seed = int(sys.argv[1])
    tamaño_tabl = int(sys.argv[2])
    tamaño_pobl = int(sys.argv[3])
    prob_cruza = float(sys.argv[4])
    prob_mut = float(sys.argv[5])
    num_ite = int(sys.argv[6])
    print("seed: ", seed)
    print("tamaño_tabl: ", tamaño_tabl)
    print("tamaño_pobl : ", tamaño_pobl)
    print("prob_cruza : ", prob_cruza)
    print("prob_mut : ", prob_mut)
    print("num_ite : ", num_ite)
else:
    print('Error en la entrada de los parametros')
    print('Los paramentros a ingresar son: semilla TamañoTablero TamañoPoblación ProbabilidadCruza ProbabilidadMutación NumeroIteración')
    sys.exit(0)

np.random.seed(seed)


print(pobl_inicial(tamaño_tabl, tamaño_pobl))







# tiempo ejecución
end = time.time()
print('Tiempo de ejecución:', end - start,'segundos')


