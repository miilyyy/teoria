import matplotlib as plt

#Datos
x= [1,2,3,4,5]
y= [10,20,30,40,50]

#Crear grafico
plt.plot(x,y)

#etiqueta de texto
plt.xlaber("Eje x:")
plt.ylabel("Eje y:")
plt.tittle("Grafico de ejemplo")


#mostrar
plt.show()

import matplotlib.pyplot as plt

label = ['a', 'b', 'c', 'd']
datos = [25, 35, 20, 20]
colores = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']    

plt.pie(datos, labels=label, colors=colores, autopct="%1.1f%%", startangle=140)
plt.axis("equal")
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10]
y=[2,5,8,11,17,21,24,27,31,34]
plt.scatter(x,y)
color=("blue")
marker="0"
plt.xlabel("eje x: ")
plt.ylabel("eje y: ")
plt.show()
