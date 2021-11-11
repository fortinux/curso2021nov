# Un ejemplo creando un directorio en la carpeta inicio del usuario:
from pathlib import Path
import os

# Se obtiene el directorio inicio del usuario en SO Linux y Windows
fichero_path = Path(Path.home(), "directorio_ficheros")
print(Path.home())
# Si no existe el directorio, se crea
if not fichero_path.exists():
    os.makedirs(fichero_path)

# Se agrego el fichero al path
fichero_path = fichero_path.joinpath("quijote-ext03.txt")

# se escriben las siguientes líneas en el fichero
with fichero_path.open('w') as file:
    lineas = [
        "Primera parte del ingenioso hidalgo don Quijote de la Mancha \n"
        "Capítulo primero. Que trata de la condición y ejercicio del famoso \n"
        "hidalgo don Quijote \n"
    ]
    file.writelines(lineas)
