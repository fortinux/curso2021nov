import platform

print("Sistema operativo: ", platform.system())
print("Versión plataforma:", platform.release())
print("Versión SO: ", platform.version())
print("Identificación del SO: ", platform.release())
print("Arquitectura: ", platform.machine())
print("Procesador: ", platform.processor())
print("Versión del Linux Kernel: ", platform.platform())
print("-------")

if platform.system() == 'Linux':
    print("Linux Rocks")
elif platform.system() == 'Darwin':
    print("Mac")
elif platform.system() == 'Win':
    print("Windows")
print("-------")

print("Versión de Python: ", platform.python_version())
print("Compilación: ", platform.python_build())
print("Compilador: ", platform.python_compiler())
print("Implementación: ", platform.python_implementation())
print("-------")