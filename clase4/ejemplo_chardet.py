# Ejemplo utilizando la biblioteca cChardet
# Adaptado de https://pypi.org/project/cchardet/

>>> import cchardet as chardet
>>> with open(r'catalogo_cf.csv', 'rb') as f:
...     msg = f.read()
...     result = chardet.detect(msg)
...     print(result)
...
{'encoding': 'ISO-8859-1', 'confidence': 0.8832640051841736}