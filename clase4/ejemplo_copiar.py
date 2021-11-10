import os
import shutil
#
# # Copiar ficheros situados en el mismo directorio
# shutil.copy(src="quijote-ext01.txt", dst="quijote-ext02.txt")
#
# # Copiar ficheros preservando los metadatos
# shutil.copy2(src="quijote-ext01.txt", dst="quijote-ext04.txt")

# # Copiar al igual que el comando cp -R en GNU/Linux
# shutil.copytree(src="../clase1/", dst="../clase1copia/")
#
# # Ignorar ficheros .jpg al copiar
# shutil.copytree(src="../clase1/", dst="../clase2copia/", ignore= shutil.ignore_patterns('*.spec'))

# Mover (o cambiar de nombre al fichero) al igual que el comando mv en GNU/Linux
# shutil.move(src="../main.py", dst="../clase1copia/main_copia.py")

# # Mover un fichero usando la biblioteca os
os.rename("../imagen.jpg", "directorio1/imagen.jpg")
#
# # Borrar un fichero
# os.remove("directorio1/imagen.jpg")