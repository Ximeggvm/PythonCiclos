def main():
    #escribe tu código abajo de esta línea.
def p_a():
    altura=int(input("Dame la altura de la piramide: "))
    ast=1
    for espacios in range (altura,0,-1):
        print((espacios-1)*" ",ast*"*",end="\n")
        ast= ast+2
    return (" ")

print(p_a())

if __name__=='__main__':
    main()
