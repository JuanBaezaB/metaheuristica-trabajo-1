import numpy as np
import time
import sys

start = time.time()


def ruleta(fit):
    n = sum(fit)
    prop = []
    for i in fit:
        prop.append(i/n)
    rulet = []
    rulet.append(prop[0])
    for i in range(1, len(prop)):
        rulet.append(rulet[i-1]+prop[i])
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
                j += 1
            i += 1
            j = i + 1
        population += 1
        if count != 0:
            list.append(1/count)
        else:
            list.append(0)
        count = 0
    return list

def crossingOver():
    children = []
    crossChildren1 = initialPop[cruza[0]]
    crossChildren2 = initialPop[cruza[1]]
    children = np.array([crossChildren1, crossChildren2])
    randomChromosome = int(np.random.random(1)[0]*(tamaño_tabl-1))
    for i in range(randomChromosome):
        aux = children[[0][0]][i]
        children[[0][0]][i] = children[[1][0]][i]
        children[[1][0]][i] = aux
    children = rectification(children)
    return children


def rectification(children):
    rows, columns= children.shape
    index = np.arange(0,columns)
    for j in range(rows):
            while True:
                rep = [x for i, x in enumerate(children[j]) if x in children[j][:i]] # Elementos repetidos
                msg = [i for i in index if i not in children[j]] # Elementos faltantes
                if len(rep): # revisamos si existen elementos repetidos
                    np.random.shuffle(index)
                    for k in index:
                        if children[j][k] in rep: # revisamos si el elemento esta dentro de los repetidos
                            rep.remove(children[j][k])
                            children[j][k] = np.random.choice(msg,1)
                            msg.remove(children[j][k])
                else:
                    break
    return children
            
def mutation(sons):
    saveSons = []
    rows, columns= sons.shape
    for son in sons:
        if np.random.rand() < prob_mut:
            while True:
                a = np.random.randint(0, columns)
                b = np.random.randint(0, columns)
                if a != b:
                    break
            son[[a,b]] = son [[b,a]]
        saveSons = np.append(saveSons, son)
    return saveSons
    


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
    print("semilla: ", seed)
    print("tamaño_tablero: ", tamaño_tabl)
    print("tamaño_población: ", tamaño_pobl)
    print("probabilidad_cruza: ", prob_cruza)
    print("probabilidad_mutación: ", prob_mut)
    print("número_iteraciones: ", num_ite)
else:
    print('Error en la entrada de los parametros')
    print('Los paramentros a ingresar son: semilla TamañoTablero TamañoPoblación ProbabilidadCruza ProbabilidadMutación NumeroIteración')
    sys.exit(0)

np.random.seed(seed)

initialPop = pobl_inicial(tamaño_tabl, tamaño_pobl)
while 1:
    fit = fitness(initialPop)
    if 0 in fit or num_ite == 0:
        break
    num_ite -= 1
    rulet = [0]
    rulet = np.append(rulet, ruleta(fit))
    sons = []
    while int(len(sons)/tamaño_pobl) < tamaño_pobl:
        if np.random.random(1)[0] < prob_cruza:
            cruza = []
            while len(cruza) < 2:
                select_rulet = np.random.random(1)[0]
                result = np.where(rulet < select_rulet)
                if result[0][-1] not in cruza:
                    cruza.append(result[0][-1])
            newChildren = crossingOver()
            newChildren = mutation(newChildren)
            if int(len(sons)/tamaño_pobl) + 2 > tamaño_pobl:
                if np.random.random(1)[0] < 0.5:
                    sons = np.append(sons, newChildren[0])
                else:
                    sons = np.append(sons, newChildren[1])
            else:
                sons = np.append(sons, newChildren)
    sons = np.resize(sons, (tamaño_pobl, tamaño_tabl))
    sons = sons.astype(int)
    initialPop = np.resize(initialPop, (tamaño_pobl, tamaño_tabl))
    initialPop = sons.astype(int)
pos = np.where(np.array(fit) == 0)
if len(pos[0]) > 0:
    print("Solucion:", initialPop[pos[0]], sep=' ')
else:

    print("No se encontro solucion")
    print("La mejor solución encontrada es:", initialPop[int(1/np.amax(fit))],"con un total de", int(1/np.amax(fit)), "choques")
# tiempo ejecución
end = time.time()
print('Tiempo de ejecución:', end - start,'segundos')