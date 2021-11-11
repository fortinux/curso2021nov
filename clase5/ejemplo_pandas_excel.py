import pandas as pd
#
# leer_fichero = pd.read_csv(r' ./catalogo_cf.csv', encoding="ISO-8859-1")
# leer_fichero.to_excel(r'./catalogo_cf.xlsx', index=None, header=True)

# Se crea el dataframe con pandas de un fichero Excel
dataframe_excel = pd.read_excel("catalogo_cf.xlsx")
print(dataframe_excel)

# Selecciona la primera y la cuarta columna
print(dataframe_excel.iloc[:, [0, 3]])

# se exporta a excel
dataframe_excel.iloc[:, [0, 3]].to_excel('catalogo_cf_resumen.xlsx')
