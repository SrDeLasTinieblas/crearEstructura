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
def estructuraDeColores():
   #imprimir("34", "Estructura de carpetas:")
   estructura = [ ("MyApplication", None),
    ("├── app", None),
    ("│   ├── src", None),
    ("│   │   ├── main", None),
    ("│   │   │   ├── AndroidManifest", "xml"),
    ("│   │   │   ├── java", None),
    ("│   │   │   │   ├── data", None),
    ("│   │   │   │   │   ├── database", None),
    ("│   │   │   │   │   │   └── MyDatabase", "java"),
    ("│   │   │   │   │   ├── models", None),
    ("│   │   │   │   │   │   ├── User", "java"),
    ("│   │   │   │   │   │   └── Product", "java"),
    ("│   │   │   │   │   └── repositories", None),
    ("│   │   │   │   │       ├── UserRepository", "java"),
    ("│   │   │   │   │       └── ProductRepository", "java"),
    ("│   │   │   │   ├── di", None),
    ("│   │   │   │   │   └── AppComponent", "java"),
    ("│   │   │   │   ├── ui", None),
    ("│   │   │   │   │   ├── activities", None),
    ("│   │   │   │   │   │   ├── MainActivity", "java"),
    ("│   │   │   │   │   │   └── ProductDetailActivity", "java"),
    ("│   │   │   │   │   │   └── ProductAdapter", "java"),
    ("│   │   │   │   │   ├── fragments", None),
    ("│   │   │   │   │   │   ├── HomeFragment", "java"),
    ("│   │   │   │   │   │   └── ProductFragment", "java"),
    ("│   │   │   │   │   ├── viewmodels", None),
    ("│   │   │   │   │   │   ├── UserViewModel", "java"),
    ("│   │   │   │   │   │   └── ProductViewModel", "java"),
    ("│   │   │   │   │   ├── dialogs", None),
    ("│   │   │   │   │   │   ├── ConfirmDialog", "java"),
    ("│   │   │   │   │   │   ├── OnProductClickListener", "java"),
    ("│   │   │   │   │   │   └── OnUserClickListener", "java"),
    ("│   │   │   │   └── utils", None),
    ("│   │   │   │   │       └── ImageUtils", "java"),
    ("│   │   │   │   └── MyApplication", "java"),
    ("│   │   │   └── res", None),
    ("│   │   │       ├── drawable", None),
    ("│   │   │       ├── layout", None),
    ("│   │   │       ├── mipmap", None),
    ("│   │   │       └── values", None),
    ("│   │   │           ├── colors", "xml"),
    ("│   │   │           ├── strings", "xml"),
    ("│   │   │           └── styles", "xml"),
    ("│   │   └── test", None),
    ("│   └── build", "gradle"),
    ("├── Gradle Scripts", None),
    ("│   ├── build", "gradle"),
    ("│   ├── gradle", None),
    ("│   └── settings", "gradle"),
    ("├── build", None),
    ("├── REAaaaDME", "md"),
    ("├── LICENSE", "ninguno"),
    ("└── ", "gitignore")
]
   
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


