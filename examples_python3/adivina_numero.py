# un juego de adivinar el numero
import random

intentosRealizados = 0

print('Hola ¿Como te llamas?')
miNombre = input()

numero = random.randint(1,20)
print('Bueno' + miNombre + 'estoy pensando un numero entre 1 y 20')

while intentosRealizados < 6:
    print('Intenta adivinar.')
    estimacion = input()
    estimacion = int(estimacion)

    intentosRealizados = intentosRealizados + 1

    if estimacion < numero:
        print('tu estimacion es muy baja')
    if estimacion > numero:
        print('tu estimacion es muy alta')
    if estimacion == numero:
        break;

if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print('buen trabajo '+ miNombre+' has adivinado el numero en '+intentosRealizados+' intentos')

if estimacion != numero:
    numero = str(numero)
    print('pues no. el numero que estaba pensando era'+ numero)
    
