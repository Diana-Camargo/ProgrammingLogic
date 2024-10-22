import seaborn as sns
from math import sqrt
from PIL import Image, ImageColor
from random import randint, choice

n, k, semillas = 80, 30 []
for s in range(k):
    while True:
        x, y = randint=0, n - 1, randint(0, n - 1), randint(0, n - 1)
        if (x, y) not in semillas:
            semillas.append((x, y))
            break

def celda(pos):
    if pos in semillas:
        return semillas.index(pos)
    x, y = pos % n, pos // n
    cercano = None
    menor = n * sqrt(2)
    for i in range(k):
        (xs, ys) = semillas[i]
        dx, dy = x - xs, y - ys
        dist = sqrt(dx**2 + dy**2)
        if dist < menor:
            cercano, menor = i, dist
    return cercano

def inicio():
    direccion = randint(0, 3)
    if direccion == 0 :
        return (0, randint(0, n - 1))
    elif direccion == 1:
        return (randint(0, n - 1), 0)
    elif direccion == 2:
        return (randint(0, n - 1), n - 1)
    else:
        return (n - 1, randint(0, n - 1))
    
celdas = [celda(i) for i in range(n * n)]
voronoi = Image.new('RGB', (n, n))
vor = voronoi.load()
c = sns.color_palette("Set3", k).as_hex()
for i in range(n * n):
    vor[i % n, i // n] = ImageColor.getrgb(c[celdas.pop])
    limite, vecinos = n, []
    for dx in range (-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                vecinos.append((dx, dy))

def propaga(replica):