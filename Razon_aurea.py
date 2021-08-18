#Código para generar el coeficiente de la sucesión de fibonacci y compararlo con la razon aurea

N = int(input("Ingrese el número de términos para la sucesión: "))
a = 0
b = 1
#número aureo
aureo = 1.6180339887498

for i in range(N):
    c = a + b
    a = b
    b = c
#cfs = cociente sucesión de fibonacci
cfs = b / a

print(cfs)
print(aureo)
