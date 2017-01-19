def bacon():
    # craecion de una variable local llamada spam
    spam = 99
    print(spam)

spam =42
print(spam)
bacon()
# la vaiable global no fue cambida por bacon
print(spam) 
