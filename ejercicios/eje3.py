#calcular la distancia
from math import *
x1=float(raw_input('Punto 1 de coordenada x'))
y1=float(raw_input('punto 1 de coordenada y'))
x2=float(raw_input('punto 2 de coordenada x'))
y2=float(raw_input('punto 2 de coordenada y'))

dx=x2-x1
dy=y2-y1
distancia=sqrt(dx**2+dy**2)
print 'la distancia entre dos puntos es ',distancia
