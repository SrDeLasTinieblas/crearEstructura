import os, sys, time
import errno
from libs.effects  import loading_effect #as effects
from libs.effects  import imprimir

#from colorama import Fore, init

#path = input("Introduzca la direccion path del proyecto: ")


'''
imprimir("34", "Estructura de carpetas:")
imprimir("1;38;2;255;215;0", "MyApplication/")
imprimir("1;38;2;255;215;0", "├── app/")
imprimir("1;38;2;255;215;0", "│   ├── src/")
imprimir("1;38;2;255;215;0", "│   │   ├── main/")
imprimir("38;2;135;206;250", "│   │   │   ├── AndroidManifest.xml")
imprimir("1;38;2;255;215;0", "│   │   │   ├── java/")
imprimir("1;38;2;255;215;0", "│   │   │   │   ├── data/")
imprimir("1;38;2;255;215;0", "│   │   │   │   │   ├── database/")
imprimir("38;2;255;160;122", "│   │   │   │   │   │   └── MyDatabase.java")
imprimir("1;38;2;255;215;0", "│   │   │   │   │   ├── models/")
imprimir("38;2;255;160;122", "│   │   │   │   │   │   ├── User.java")
imprimir("38;2;255;160;122", "│   │   │   │   │   │   └── Product.java")
imprimir("1;38;2;255;215;0", "│   │   │   │   │   └── repositories/")
imprimir("38;2;255;160;122", "│   │   │   │   │       ├── UserRepository.java")
imprimir("38;2;255;160;122", "│   │   │   │   │       └── ProductRepository.java")
imprimir("1;38;2;255;215;0", "│   │   │   │   ├── di/")
imprimir("38;2;255;160;122", "│   │   │   │   │   └── AppComponent.java")
imprimir("1;38;2;255;215;0", "│   │   │   │   ├── ui/")
imprimir("1;38;2;255;215;0", "│   │   │   │   │   ├── activities/")
imprimir("38;2;255;160;122", "│   │   │   │   │   │   ├── MainActivity.java")
imprimir("38;2;255;160;122", "│   │   │   │   │   │   └── ProductDetailActivity.java")
imprimir("38;2;255;160;122", "│   │   │   │   │   │   └── ProductAdapter.java")
imprimir("1;38;2;255;215;0", "│   │   │   │   │   ├── fragments/")
imprimir("38;2;255;160;122", "│   │   │   │   │   │   ├── HomeFragment.java")
imprimir("38;2;255;160;122", "│   │   │   │   │   │   └── ProductFragment.java")
imprimir("1;38;2;255;215;0", "│   │   │   │   │   ├── viewmodels/")
imprimir("38;2;255;160;122", "│   │   │   │   │   │   ├── UserViewModel.java")
imprimir("38;2;255;160;122", "│   │   │   │   │   │   └── ProductViewModel.java")
imprimir("1;38;2;255;215;0", "│   │   │   │   │   ├── dialogs/")
imprimir("38;2;255;160;122", "│   │   │   │   │   │   └── ConfirmDialog.java")
imprimir("38;2;255;160;122", "│   │   │   │   │   │   ├── OnProductClickListener.java")
imprimir("38;2;255;160;122", "│   │   │   │   │   │   └── OnUserClickListener.java")
imprimir("1;38;2;255;215;0", "│   │   │   │   └── utils/")
imprimir("38;2;255;160;122", "│   │   │   │   │       └── ImageUtils.java")
imprimir("38;2;255;160;122", "│   │   │   │   └── MyApplication.java")
imprimir("1;38;2;255;215;0", "│   │   │   └── res/")
imprimir("1;38;2;255;215;0", "│   │   │       ├── drawable/")
imprimir("1;38;2;255;215;0", "│   │   │       ├── layout/")
imprimir("1;38;2;255;215;0", "│   │   │       ├── mipmap/")
imprimir("1;38;2;255;215;0", "│   │   │       └── values/")
imprimir("38;2;135;206;250", "│   │   │           ├── colors.xml")
'''

estructura = [ 
    ("MyApplication", None),
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
    ("├── README", "md"),
    ("├── LICENSE", "ninguno"),
    ("└── ", "gitignore")
]


ruta_archivos_padres = [
    ("data", None),
    ("di", None),
    ("ui", None),
    ("utils", None),
    ("MyApplication", "java")
]

ruta_archivos_hijos = [
    ("data", None),
    ("database", None),
    ("MyDatabase", "java")
]

ruta_base = "java/"

'''def createFileJava(path, file, ext):
    file = open(path + file+ ext, "w")
    file.write("package com.tinieblas.tokomegawa.ui.fragments;\n \n")
    file.write("public class HomeFragment {\n")
    file.write("}")
    file.close()'''

'''for nombre, extension in ruta_archivos_padres:
    if extension:
        # Crear archivo
        with open(os.path.join(ruta_base, nombre + "." + extension), "w") as archivo:
            archivo.write("Este es el contenido del archivo.")
            print(ruta_base)
            print(nombre)
            print(extension)
            print("Done.")
    else:
        # Crear carpeta
        if not os.path.exists(os.path.join(ruta_base, nombre)):
            # Si no existe, crearla
            os.makedirs(os.path.join(ruta_base, nombre))
        else:
            print("La carpeta ya existe.")

        #createFileJava(ruta_base, nombre, extension)
        #with open(os.path.join(ruta_base, "MyAplication" + "." + extension), "w"):
            #archivo.write("Este es el contenido del archivo.")
'''

ruta_base = "java/"

# Se crea la carpeta base
os.makedirs(ruta_base, exist_ok=True)

# Se recorre la lista y se crean las carpetas y archivos correspondientes
ruta_actual = ruta_base
for nombre, extension in ruta_archivos_hijos:
    # Se verifica si es una carpeta
    if extension is None:
        ruta_actual = os.path.join(ruta_actual, nombre)
        os.makedirs(ruta_actual, exist_ok=True)
    # Si no es una carpeta, se asume que es un archivo
    else:
        ruta_archivo = os.path.join(ruta_actual, nombre + "." + extension)
        with open(ruta_archivo, "w") as archivo:
            pass # Aquí se podría escribir el contenido del archivo si se desea





'''for nombre, extension in ruta_archivos_hijos:
    
    if not extension:
        # Crear carpeta
        os.makedirs(os.path.join(ruta_base, nombre), exist_ok=True)
        #if not os.path.exists(os.path.join(path_completo)):
            # Si no existe, crearla
            #  print(path_completo)
        print("Crear carpeta")
            

    else:
        # Crear carpeta
        path_completo = ruta_base + nombre
        print("Crear archivo")
        #'''


'''for nombre, extension in ruta_archivos_hijos:
    path_completo = ruta_base + nombre + str(extension)
    if extension:
        # Crear archivo
        with open(os.path.join(path_completo, nombre + "." + extension), "w") as archivo:
            print(path_completo)
            #archivo.write("Este es el contenido del archivo.")
            print("Crear archivo")
          #  print(ruta_base + nombre + extension)
           # print("Done.")
    else:
        # Crear carpeta
        if not os.path.exists(os.path.join(path_completo)):
            # Si no existe, crearla
            print(path_completo)
            print("Crear carpeta")
            #os.makedirs(os.path.join(path_completo, nombre))
        else:
            print(ruta_base + nombre)
            print("La carpeta ya existe.")'''

        #createFileJava(ruta_base, nombre, extension)
        #with open(os.path.join(ruta_base, "MyAplication" + "." + extension), "w"):
            #archivo.write("Este es el contenido del archivo.")


'''
CON ESO SALE LOS COLORES
---
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
        imprimir('1;38;2;255;215;0', nombre + '/')'''




#loading_effect(100)
'''try:
    path = os.makedirs('data/database')
    path = os.makedirs('data/models')
    path = os.makedirs('di/repositories')
    path = os.makedirs('data/repositories')
    path = os.makedirs('data/repositories')
    path = os.makedirs('data/repositories')
    path = os.makedirs('data/repositories')


except OSError as e:
   if e.errno != errno.EEXIST:
       raise
'''

#try:

'''createFileJava("data/models", "User", ".java")'''

#os.mkdir('dir2')
#os.mkdir('dir3')
#os.mkdir('dir4')
    #print(path)
#except OSError as e:
 #   if e.errno != errno.EEXIST:
  #      raise

#package com.tinieblas.tokomegawa.ui.fragments;

#public class HomeFragment {
#}


















