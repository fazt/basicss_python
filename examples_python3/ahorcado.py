import random

IMAGENES_AHORCADO = ['''
    +---+
    |
        |
        |
        |
        |
        |
     =========''', '''
    +---+
    |   |
    O
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O
    |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O
    |
   /|
        |
        |
        |
    =========''', '''
     +---+
     |   |
     O
     |
    /|\  |
         |
         |
    =========''', '''
     +---+
     |  |
     O
     |
    /|\ |
    /
        |
        |
    =========''', '''
     +---+
     |  |
     O
     |
    /|\ |
    / \ |
        |
========='''];

palabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split()

def obtenerPalabraAlAzar(listaDePalabras):
    indiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[indiceDePalabras]

def mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(IMAGENES_AHORCADO[len(letrasIncorrectas)])
    print()

    print('Letras Incorrectas: ',end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()

    espaciosVacios = '_' * len(palabraSecreta)

    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacios = espaciosVacios[:i] + palabraSecreta[i] + espaciosVacios[i+1:]
    for letra in espaciosVacios:
        print(letra, end='')
    print()

def obtenerIntento(letrasProbadas):
    #return the player's letter, just one letter and not other things
    while True:
        print('Guess a Letter')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Please, just ONE letter')
        elif intento in letrasProbadas:
            print('You have try this letter, try another.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Plase type a letter')
        else:
            return intento

# ININITIALIZATION OF THE GAME
print('A H O R C A D O')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta = obtenerPalabraAlAzar(palabras)
juegoTerminado = False

# THE GAME LOOP
while True:
    mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
    #allot to the player type a letter
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)
    if intento in palabraSecreta:
        letrasCorrectas += intento
        #verify if the player won
        encontrandTodaslasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontrandTodaslasLetras = False
                break
        if encontrandTodaslasLetras:
            print('sí, La palabra secreta es "' + palabraSecreta + '"! Has ganado' )
            juegoTerminado = True
    else:
