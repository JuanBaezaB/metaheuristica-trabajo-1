import numpy as np
import time
import sys

def ruleta(fit):
    n = sum(fit)
    prop = []
    for i in fit:
        prop.append(i/n)
    rulet = []
    rulet.append(prop[0])
    for i in range(1, len(prop)):
        rulet.append(rulet[i-1]+prop[i])
    print(rulet)
    return rulet



def fitness(tablero):
    population = 0
    count = 0
    list = []
    while population < tamaño_pobl:
        i = 0
        j = 1
        while i<tamaño_pobl-1:
            while j<tamaño_tabl:
                if abs(tablero[population][i]-tablero[population][j]) == abs(i-j):
                    count += 1
                    # print("Colisiones: " + str(i) + " " + str(tablero[population][i]) + " " + str(j) + " " + str(tablero[population][j]))
                j += 1
            i += 1
            j = i + 1
        population += 1
        list.append(count)
        count = 0
    return list

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

#print(fitness(pobl_inicial(tamaño_tabl, tamaño_pobl)))
fit = fitness(pobl_inicial(tamaño_tabl, tamaño_pobl))


while 0 not in fit:
    rulet = ruleta(fit)
    select_rulet = np.random.random(1)[0]
    


# tiempo ejecución
end = time.time()
print('Tiempo de ejecución:', end - start,'segundos')