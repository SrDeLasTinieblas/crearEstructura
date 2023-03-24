import os, sys, time
from colorama import Fore, init


def imprimir(color, cadena):
    print(f"\033[{color}m{cadena}\033[0m")

def loading_effect(time):
  KEYS = ["/","-","\\"];
  
  cont = 0
  time_2 = 1

  while(time_2 < time):
    for key in KEYS:
        os.system('cls')
        print(key)

        if cont <= 1:
          cont+=1
        else:
          cont=0
    time_2+=1
  os.system('cls')
  print("The process has been completed satisfactorily!")


#CON ESO SALE LOS COLORES
'''
def estructuraDeColores():
    for nombre, extension in estructura:
        if extension == 'java':
            imprimir('38;2;255;160;122', f"{nombre}.{extension}")
        elif extension == 'xml':
           imprimir('38;2;135;206;250', f"{nombre}.{extension}")
        elif extension == 'gradle':
            imprimir("33", f"{nombre}.{extension}")
        elif extension == 'md':
            imprimir("38;2;135;206;250", f"{nombre}.{extension}")
        elif extension == 'ninguno':
            imprimir("38;2;255;160;122", f"{nombre}.{extension}")
        elif extension == 'gitignore':
            imprimir("38;2;255;215;0", f"{nombre}.{extension}")

    else:
        imprimir('1;38;2;255;215;0', nombre + '/')
'''
