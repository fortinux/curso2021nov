import re

texto = "Hoy es un día magnífico y maravilloso"
exp_reg = re.search("^Hoy.*", texto)
print(exp_reg)

exp_reg2 = re.findall("ma", texto)
print(exp_reg2)

exp_reg3 = re.sub("\s", "    ", texto)
print(exp_reg3)
