a=float(raw_input("Valor de a "))
b=float(raw_input("Valor de b"))

if a!=0:
    x=-b/a
    print "solucion ",x
else:
    if b!=0:
        print "la ecuacion no tiene solucion"
    else:
        print "la ecuacion tiene infinitas solucioess"
