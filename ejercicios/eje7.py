from math import pi
opcion=0
while opcion !=4:
    print 'Escoge una opcion: '
    print '1)calcular el Diametro'
    print '2)calcular el perimetro'
    print '3)calcular el area'
    print '4)salir'
    opcion=int(raw_input('teclea 1, 2, 3 o 4 y pulsa enter: '))
    radio=float(raw_input('dame el radio del circulo: '))

    if opcion == 1:
        diametro = 2 * radio
        print 'el diametro es ',diametro
    elif opcion ==2:
        perimetro=2*pi*radio
        print 'el perimetro es ',perimetro
    elif opcion ==3:
        area=pi*radio**2
        print 'el area es ',area
    elif opcion <0 or opcion >4:
        print 'solo hay cuatro opciones 1,2,3,4. tu has tecleado ',opcion
