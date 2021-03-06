from random import randint
from random import shuffle

def valores (val):
    if val=='A':
        return 1
    elif val=='2':
        return 2
    elif val=='3':
        return 3
    elif val=='4':
        return 4
    elif val=='5':
        return 5
    elif val=='6':
        return 6
    elif val=='7':
        return 7
    elif val=='8':
        return 8
    elif val=='9':
        return 9
    elif val=='J'or val=='K'or val=='Q':
        return 10
    
def valoresEspeciales (lista):
        if dimensionLista(lista)<48:
                if lista==[]:
                        lista.append('A')
                        return valoresEspeciales(lista)
                elif lista[-1]=='A':
                        lista.append('2')
                        return valoresEspeciales(lista)
                elif lista[-1]=='9':
                        lista.append('J')
                        return valoresEspeciales(lista)
                elif lista[-1]=='J':
                        lista.append('Q')
                        return valoresEspeciales(lista)
                elif lista[-1]=='Q':
                        lista.append('K')
                        return valoresEspeciales(lista)
                elif lista[-1]=='K':
                        lista.append('A')
                        return valoresEspeciales(lista)
                elif int(lista[-1])<9:
                        lista.append(str(int(lista[-1])+1))
                        return valoresEspeciales(lista)
        else:
                return lista
            
def dimensionLista(lista):
        if lista==[]:
                return 0
        else:
                return 1 + dimensionLista(lista[1:])
    

def repartirCartas(num,lista,s):
        if num==21:
                return num
        if num==-1:
                return -1 
        elif num<21:
                print ("\nInserte 'SI' para recibir mas cartas y 'NO' para plantarse?")
                if raw_input()=="NO":
                        print ("\nTURNO DEL CPU")
                        if turnoCPU(0,num,lista)==0:
                                return -1
                        else:
                                return num
                else:
                    shuffle(lista)
                    if lista[0]=='A':
                        if num+11>21:
                            print("\nNueva Carta: ")
                            print lista[0]
                            print ("Total de Cartas:")
                            print num+valores(lista[0])
                            return repartirCartas(num+valores(lista[0]),lista,s)
                        else:
                            print("\nNueva Carta: ")
                            print lista[0]
                            print ("Total de Cartas:")
                            print num+valores(lista[0])
                            return repartirCartas(num+11,lista,s+1)
                    print("\nNueva Carta: ")
                    print lista[0]
                    print ("Total de Cartas:")
                    print num+valores(lista[0])
                    return repartirCartas(num+valores(lista[0]),lista,s)
        elif num>21&s==0:
                return -1
        elif num>21&s>0:
                 print ("A reducida : Nueva suma de cartas = ",num-10)
                 return repartirCartas(num-10,lista,s-1)
            
    
def turnoCPU(num,user,lista):
        if (num<21)&(num>user):
                return 0
        if num==21:
                return 0
        if num > 21:
                return 1
        if num<21:
                shuffle(lista)
                print("\nNueva Carta: ")
                print lista[0]
                print ("Total de Cartas:")
                print num+valores(lista[0])
                return turnoCPU(num+valores(lista[0]),user,lista)

def main():
    print ("JUEGO DE 21")
    print ("\nTURNO DEL JUGADOR")
    print ("\nInserte 'SI' para recibir mas cartas y 'NO' para plantarse")

    if repartirCartas(0,valoresEspeciales(lista=[]),0)==(-1):
        print("\nHAS PERDIDO!")
    else:
        print("\nHAS GANADO!")
if __name__ == "__main__":
    main()
