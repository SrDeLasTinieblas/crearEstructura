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


