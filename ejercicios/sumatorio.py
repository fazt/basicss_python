from math import *
#pedir limites inferior y superior
a=int(raw_input('limite inferior: '))
while a<0:
    print 'No ingreses numeros negativos'
    a=int(raw_input('limite inferior: '))

b=int(raw_input('limite superior: '))
while b<0:
    print 'No ingreses numeros negativos'
    a=int(raw_input('limite superior: '))

#calcular la sumatoria
s=0.0
for i in range(a,b+1):
    print i
    s+=sqrt(i)


print 'sumatoria de raices'
print 'de %d hasta %d: %f' %(a,b,s)
