import pandas as pd

df=pd.read_csv("")

#print(df.head())
#print(df.tail(20)) #mostrar pie
#print (df.to_string()) #muetra todo
#print(df.shape) #tira dos numeros, cantidad de filas y columnas.
#print(df.dtypes) #mostrar ostipos de dato
#print(f.info()) #muestra dato sin completar (no null), para limpiar
#print-(df.describe()) #da datos estadisticas de la tabla

print(df{"gender","lunch"}.head()) #muestra una columna