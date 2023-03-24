import os, sys, time, re
import errno
from libs.effects  import loading_effect #as effects
from libs.effects  import imprimir
from libs.effects  import estructuraDeColores

#path = input("Introduzca la direccion path del proyecto: ")
path = "java/"

ruta_archivos = [
    ("data/", None),
    ("data/database", None),
    ("data/database/MyDatabase", "java"),
    ("data/models", None),
    ("data/models/User", "java"),
    ("data/models/Product", "java"),
    ("data/repositories", None),
    ("data/repositories/UserRepository", "java"),
    ("data/repositories/ProductRepository", "java"),
    ("di/", None),
    ("di/AppComponent", "java"),
    ("ui/", None),
    ("ui/activities", None),
    ("ui/activities/MainActivity", "java"),
    ("ui/activities/ProductDetailActivity", "java"),
    ("ui/activities/ProductAdapter", "java"),
    ("ui/fragments", None),
    ("ui/fragments/HomeFragment", "java"),
    ("ui/fragments/ProductFragment", "java"),
    ("ui/viewmodels", None),
    ("ui/viewmodels/UserViewModel", "java"),
    ("ui/viewmodels/ProductViewModel", "java"),
    ("ui/dialogs", None),
    ("ui/dialogs/ConfirmDialog", "java"),
    ("ui/dialogs/OnProductClickListener", "java"),
    ("ui/dialogs/OnUserClickListener", "java"),
    ("utils/", None),
    ("utils/ImageUtils", "java")
    #("MyApplication", "java")
]

estructuraDeColores()

# Ruta base donde se crearan los archivos y carpetas
path = "java/"
def generar_archivos_directorios():

    nombre_package = input("package com.nombre.nombre.ui.ativities\nIntroduzca el nombre de su package: ")
    for folder, extension in ruta_archivos:
        folder_path = os.path.join(path, folder)
    
        # Verificar si la carpeta ya existe
        if os.path.isdir(folder_path):
            print(f"La carpeta {folder_path} ya existe")
        else:
            os.makedirs(folder_path)
            print(f"Se creó la carpeta {folder_path}")
    
        # Crear archivo si se especificó una extensión
        if extension:
            file_path = os.path.join(folder_path, folder.split("/")[-1] + "." + extension)
        
            # Verificar si el archivo ya existe
            if os.path.isfile(file_path):
                print(f"El archivo {file_path} ya existe")
            else:
                file = open(file_path, "w")#.close()
                #file.write("package com."+ nombre_package + ".ui.fragments;\n \n")
                print(file_path)
            print(f"Se creó el archivo {file_path}")

generar_archivos_directorios()
#loading_effect(100)

'''createFileJava("data/models", "User", ".java")'''
'''def createFileJava(path, file, ext):
    file = open(path + file+ ext, "w")
    file.write("package com.tinieblas.tokomegawa.ui.fragments;\n \n")
    file.write("public class HomeFragment {\n")
    file.write("}")
    file.close()'''


















