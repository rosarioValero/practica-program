import random 
import time 
import os 

def clear(): 
    os.system("cls") 

clear() 

def gameEasy(): 
    partidas = 3 
    
    print ("\n Instrucciones: Memoriza la posición del valor X")
    time.sleep(3)
    print("\n Por ejemplo: ")
    print ("1- (x,0,0)") 
    print ("2- (0,x,0)") 
    print ("3- (0,0,x)")
    
    time.sleep(3) 
    print ("Listo") 
    time.sleep(3) 
    print ("YA") 
    time.sleep(1) 
    clear() 
    while True: 
        level = 1 
        secuencias = [("x",0,0), (0,"x",0), (0,0,"x")] 
        tempS = [] 
        intentos = [] 

        for x in range(partidas): 
            rand = random.randrange(3) 
            tempS.append(secuencias[rand]) 

        cont = 1
        for i in tempS: 
            print (cont, i)
            cont +=1
            time.sleep(2) 
            clear() 

        contador = 1 

        for j in range(partidas): 
            print ("\n Introduzca la posicion: ", contador) 
            usuario = input() 
            intentos.append(secuencias[int(usuario)-1]) 
            contador += 1 

        if intentos == tempS: 
            print ("Ganaste") 
            partidas += 1 
            print ("Subiste a ", partidas) 
            time.sleep(1) 
            print ("Listo") 
            time.sleep(1) 
            print ("ya") 
            time.sleep(1) 
        else: 
            print ("\n Perdiste \n") 
            if partidas > 2: 
                partidas -= 1 
                print ("Bajaste a ", partidas) 
                time.sleep(1) 
                print ("Listo") 
                time.sleep(1) 
                print ("ya") 
                time.sleep(1) 
            else:
                print("\n                     ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ ",
                       "\n                   ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗",
                       "\n                   ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝",
                       "\n                   ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗",
                       "\n                   ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║",
                        "\n                   ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")
                time.sleep(5)
                break 

        clear() 
    clear()
    menu()


def gameHard(): 
    partidas = 4 
    
    print ("\n Instrucciones: Memoriza la posición del valor X")
    time.sleep(3)
    print("\n Por ejemplo: ")
    print ("1- (x,0,0,0)") 
    print ("2- (0,x,0,0)") 
    print ("3- (0,0,x,0)")
    print ("4- (0,0,0,x)")
    
    time.sleep(3) 
    print ("Listo") 
    time.sleep(3) 
    print ("YA") 
    time.sleep(1) 
    clear() 
    while True: 
        level = 1 
        secuencias = [("x",0,0,0), (0,"x",0,0), (0,0,"x",0),(0,0,0,"X")] 
        tempS = [] 
        intentos = [] 

        for x in range(partidas): 
            rand = random.randrange(4) 
            tempS.append(secuencias[rand]) 

        cont = 1
        for i in tempS: 
            print (cont, i)
            cont +=1
            time.sleep(2) 
            clear() 

        contador = 1 

        for j in range(partidas): 
            print ("\n Introduzca la posicion: ", contador) 
            usuario = input() 
            intentos.append(secuencias[int(usuario)-1]) 
            contador += 1 

        if intentos == tempS: 
            print ("Ganaste") 
            partidas += 1 
            print ("Subiste a ", partidas) 
            time.sleep(1) 
            print ("Listo") 
            time.sleep(1) 
            print ("ya") 
            time.sleep(1) 
        else: 
            print ("\n Perdiste \n") 
            if partidas > 4: 
                partidas -= 1 
                print ("Bajaste a ", partidas) 
                time.sleep(1) 
                print ("Listo") 
                time.sleep(1) 
                print ("ya") 
                time.sleep(1) 
            else:
                print("\n                     ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ ",
                       "\n                   ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗",
                       "\n                   ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝",
                       "\n                   ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗",
                       "\n                   ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║",
                        "\n                   ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")
                time.sleep(5)
                break 

        clear()
    clear()
    menu()
        
        
def menu():
    print ("\n                          ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗",
           "\n                          ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝",
           "\n                          ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  ",
           "\n                          ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  ",
           "\n                          ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗",
            "\n                          ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝ ")
    

    print("\n ===========================================================")
    print("                                                           ")
    print("           1) Mode Easy                                    ")
    print("           2) Mode Hard                                    ")
    print("           3) Salir                                        ")
    print("===========================================================")


    print("Selecciona una opción: ")
    opcion = int(input())

    while opcion != 3:
        if opcion == 1:
           gameEasy()
        elif opcion == 2:
            gameHard()
        elif opcion==3:
            print('salir ')
        else:
            print('No haz introducido ninguna opción')
    return opcion


menu()

