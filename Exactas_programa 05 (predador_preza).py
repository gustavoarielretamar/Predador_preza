# %% LIBRERIAS:
import matplotlib.pyplot as plt
import numpy as np
import random
# %% TABLERO EN 0:
def crear_tablero(n, m, debug=False):
    t = np.repeat(" ", (n+2)*(m+2)).reshape((n+2), (m+2))
    if debug:
        print(t)
    return t
# %% BORDES:
def bordes(t, debug=False):
    filas = t.shape[0]
    columnas = t.shape[1]
    for i in range(0, columnas):
        t[(0, i)] = "M"
        t[(filas - 1, i)] = "M"
        i = i + 1
    for i in range(0, filas):
        t[(i, 0)] = "M"
        t[(i, columnas - 1)] = "M"
        i = i + 1
    if debug:
        print(t)
    return t
# %% AGREGO ANIMALES:
def agregar_animales(t, debug=False):
    filas = [1, 2, 2, 3, 1]
    columnas = [3, 1, 3, 1, 1]
    animal = ["A", "A", "A", "A", "L"]
    for i in range(len(animal)):
        t[(filas[i], columnas[i])] = animal[i]
    if debug:
        print(t)
    return t
# %% VECINOS DE:
def vecinos_de(t, coord, debug=False):
    vecinos = []
    f = coord[0]
    c = coord[1]
    v1 = (f-1, c-1)
    c1 = t[(f-1, c-1)] != "M"
    v2 = (f-1, c)
    c2 = t[(f-1, c)] != "M"
    v3 = (f-1, c+1)
    c3 = t[(f-1, c+1)] != "M"
    v4 = (f, c+1)
    c4 = t[(f, c+1)] != "M"
    v5 = (f+1, c+1)
    c5 = t[(f+1, c+1)] != "M"
    v6 = (f+1, c)
    c6 = t[(f+1, c)] != "M"
    v7 = (f+1, c-1)
    c7 = t[(f+1, c-1)] != "M"
    v8 = (f, c-1)
    c8 = t[(f, c-1)] != "M"
    if c1:
        vecinos.append(v1)
    if c2:
        vecinos.append(v2)
    if c3:
        vecinos.append(v3)
    if c4:
        vecinos.append(v4)
    if c5:
        vecinos.append(v5)
    if c6:
        vecinos.append(v6)
    if c7:
        vecinos.append(v7)
    if c8:
        vecinos.append(v8)
    if debug:
        print(vecinos)
    return vecinos
# %% BUSCAR ADYACENTES:
def buscar_adyacente(t, coord, objetivo, debug=False):
    adyacentes = vecinos_de(t, coord)
    respuesta = []
    j = 0
    for i in range(len(adyacentes)):
        if t[adyacentes[i]] == objetivo and j == 0:
            respuesta.append(adyacentes[i])
            j += 1
    if debug:
        print(respuesta)
    return respuesta
# %% ALIMENTARSE:
def alimentar(t, coord, debug=False):
    l = 0
    if t[coord] == "L" and l == 0:
        comer = buscar_adyacente(t, coord, "A")
        if comer:
            t[coord] = " "
            t[comer[0]] = "L"
        l += 1
    else:
        l += 1
    if debug:
        print(t)
    return t
# %% REPRODUCIRSE:
def reproducir(t, coord, debug=False):
    l = 0
    if t[coord] == "A" and l == 0:
        pareja = buscar_adyacente(t, coord, "A")
        if pareja:
            decendencia = buscar_adyacente(t, coord, " ")
            if decendencia:
                t[decendencia[0]] = "A"
        l += 1
    elif t[coord] == "L" and l == 0:
        pareja = buscar_adyacente(t, coord, "L")
        if pareja:
            decendencia = buscar_adyacente(t, coord, " ")
            if decendencia:
                t[decendencia[0]] = "L"
        l += 1
    else:
        l += 1
    if debug:
        print(t)
    return t
# %% MOVERSE:


def mover(t, coord, debug=False):
    l = 0
    if t[coord] == "A" and l == 0:
        comer = buscar_adyacente(t, coord, " ")
        if comer:
            t[coord] = " "
            t[comer[0]] = "A"
        l += 1
    elif t[coord] == "L" and l == 0:
        comer = buscar_adyacente(t, coord, " ")
        if comer:
            t[coord] = " "
            t[comer[0]] = "L"
        l += 1
    else:
        l += 1
    if debug:
        print(t)
    return t

# %% FASE ALIMENTARSE:
def fase_alimentar(t, debug=False):
    cantidad_filas = t.shape[0]
    cantidad_columnas = t.shape[1]
    for i in range(1, cantidad_filas - 1):
        for j in range(1, cantidad_columnas - 1):
            alimentar(t, (j, i))
    if debug:
        print(t)
    return t
# %% FASE REPRODUCIRSE:
def fase_reproducir(t, debug=False):
    cantidad_filas = t.shape[0]
    cantidad_columnas = t.shape[1]
    for i in range(1, cantidad_filas - 1):
        for j in range(1, cantidad_columnas - 1):
            reproducir(t, (i, j))
    if debug:
        print(t)
    return t
# %% FASE DE MOVERSE:
def fase_mover(t, debug=False):
    cantidad_filas = t.shape[0]
    cantidad_columnas = t.shape[1]
    for i in range(1, cantidad_filas - 1):
        for j in range(1, cantidad_columnas - 1):
            mover(t, (i, j))
    if debug:
        print(t)
    return t
# %% EVOLUCIONAR:
def evolucionar(t, debug = False):
    fase_alimentar(t)
    fase_reproducir(t)
    fase_mover(t)
    if debug:
        print(t)
    return t
# %% EVOLUCIONAR EN EL TIEMPO:
def evolucionar_en_el_tiempo(t, k, debug=False):
    i = 0
    while i < k:
        t = evolucionar(t)
        i += 1
    if debug:
        print(t)
# %% MEZCLAR:
def mezclar_celdas(tablero, debug = False):
    celdas = []
    for i in range (1 , len(tablero) - 1) :
        for j in range (1 , len(tablero) - 1) :
            celdas.append((i, j))
    random.shuffle(celdas)
    if debug:
        print(celdas)
    return celdas
# %% ANIMALES RANDOM:
def animales_random(t, debug=False):
    celdas = mezclar_celdas(t)
    filas = []
    columnas = []
    animal = []
    for i in range(0, len(celdas)):
        filas.append(celdas[i][0])
        columnas.append(celdas[i][1])
    for i in range(0, n_antilopes):
        animal.append("A")
    for i in range(0, n_leones):
        animal.append("L")
    for i in range(len(animal)):
        t[(filas[i], columnas[i])] = animal[i]
    if debug:
        print(t)
    return t
# %% GENERAR TABLERO AL AZAR:
def generar_tablero_azar(t, debug=False):
    bordes(t)
    animales_random(t)
    if debug:
        print(t)
# %% PARAMETROS:
n = 10
m = 10
k = 10
n_antilopes = 10
n_leones = 3

# %% LLAMADAS:
# t1 = crear_tablero(n, m)
# bordes(t1)
# # agregar_animales(t1, True)
# animales_random(t1, True)
# t2 = evolucionar(t1, True)
# evolucionar(t2, True)
# mezclar_celdas(t1, True)
t1 = crear_tablero(n, m)
generar_tablero_azar(t1, True)
evolucionar_en_el_tiempo(t1, k, True)
