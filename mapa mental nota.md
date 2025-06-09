# Markdown

- **Negrita**: `**texto**` o `__texto__`
- *Cursiva*: `*texto*` o `_texto_`
- Listas ordenadas: `1. Elemento 1`
- Listas no ordenadas: `- Elemento 1` o `* Elemento 1`
- Enlaces: `[texto](url)`
- Imágenes: `![texto alternativo](url de la imagen)`
- Encabezados: `# Título 1`, `## Título 2`, etc.
# Lista de StudentsPerformarce
- print(df)
- print(df.head()) (mostrar las primeras 5 )
- print(df.tail()) (muestra lass ultima 5 )
- print(df.to_string()) #(muestra todo)
- print(df.shape) #(cantidad de filas y columnas)
- print(df.dtypes) #(muestra los tipos de datos de cada columna)
- print(df.info()) #(muestra datos sin completar, para limpiar los datos non-null)
- print(df.describe()) #(da datos estadisticos de cada tabla)
- print(df["gender"].head()) #(muestra los generos)
- print(df[["gender","lunch"]].head()) #(muestra de columnas de la lista)
- a=np.random.randint(1,100,size=1000) #crear una columna con numeros aletorios
- print(df["math score"].sum) #suma
- print(df["math score"].count) #resta
- print(df["math score"].median) #la media
- print(df["math score"].std) #estandar
- print(df["math score"].max) #maximo
- print(df["math score"].min) #minimo
- print(df.head)
# Numpy
- Es una librería muy utilizada para cálculos numéricos y álgebra lineal. Permite trabajar con matrices, vectores y otras estructuras de datos numéricas de forma eficiente.

- Instalación:
pip install numpy
# Pandas
- Se usa principalmente para manipulación y análisis de datos. Su estructura de datos principal es el DataFrame, que facilita el manejo de datos tabulares.

- Instalación:
pip install pandas
# Matplotlib
- Es una librería para crear gráficos y visualizaciones en 2D.

- Instalación:
pip install matplotlib

# Requests:
- Esta librería se utiliza para hacer peticiones HTTP de forma sencilla.

- Instalación:
pip install requests
# Flask:
- Es un micro-framework para el desarrollo web que facilita la creación de aplicaciones web y APIs.

- Instalación:
pip install flask
# TensorFlow/PyTorch:
- Son librerías para aprendizaje automático (machine learning) y redes neuronales profundas (deep learning).

- Instalación:
pip install tensorflow o pip install torch
# Scikit-learn:
- Usada para machine learning y análisis de datos. Ofrece herramientas para clasificación, regresión, clustering y más.

- Instalación:
pip install scikit-learn
# BeautifulSoup:
- Librería para analizar documentos HTML y XML, comúnmente utilizada para hacer scraping web.

- Instalación:
pip install beautifulsoup4
Estas son solo algunas de las miles de librerías disponibles en el ecosistema Python.

## Seaborn
importar libreria y traer datos de ejemplo

    .import seaborn as sns
     import matplotlib.pyplot as plt



    datos=sns.load_dataset("tips")
    print(datos.head)
# Grafico de dipercion scatterplot 
. sns.scatterplot(data=datos,x="total_bill",y="tip")
# grafico de barras
. sns.barplot(data=datos,x="day", y="total_bill" )

. sns.histplot(data=datos,x="total_bill", bins=20)
# boxplot(grafico de caja)
. sns.boxplot(data=datos,x="day", y="total_bill" )
# Grafico de violin  
. sns.violinplot(data=datos,x="day", y="total_bill" )
# añadir titulo y etiqueta de los ejes 
. sns.scatterplot(data=datos,x="total_bill",y="tip")
  plt.title("Relacion de la calidad y la propina ")
  plt.xlabel("calidad")
  plt.ylabel("propinas")

