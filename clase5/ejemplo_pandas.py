# -*- coding: iso-8859-1 -*-
import pandas as pd


# Variables con los ficheros a importar
fichero_csv = "catalogo_cf.csv"
fichero_tsv = "catalogo_cf.tsv"

# Nombres de los ficheros a escribir
escribir_csv = 'catalogo_csv_ext.csv'
escribir_tsv = 'catalogo_tsv_ext.tsv'

# Lee los datos de los ficheros
# Para la codificación estándar europea también se puede utilizar también latin_1
leer_csv = pd.read_csv(fichero_csv, encoding="ISO-8859-1")
leer_tsv = pd.read_csv(fichero_tsv, sep='\t')

# Imprime los primeros 10 registros
print(leer_csv.head(10))
print(leer_tsv.head(10))

# Escribe en los ficheros (en el .csv solamente los 10 primeros registros)
with open(escribir_csv, 'w') as write_csv:
    # index=False no muestra el índice
    write_csv.write(leer_csv.head(10).to_csv(sep=',', index=False))

with open(escribir_tsv, 'w') as write_tsv:
    write_tsv.write(leer_tsv.to_csv(sep='\t', index=False))
