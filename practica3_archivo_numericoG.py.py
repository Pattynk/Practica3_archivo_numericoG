import turtle as t
import csv

#La imágen fue creada en Pixilart https://www.pixilart.com/art/pixilart-abejis-sr5zd29be829b8aws3 
#La matriz fue convertida con IA https://chatgpt.com/share/68d6bf28-a6ac-800c-ae10-25164fcdd2b1
#El archivo fue guardado dentro de la misma carpeta del proyecto con un formato de vector svg numérico

#Función para dibujar en otro lado sin dejar rastro al moverse
def teleport(x: float, y: float) -> None:
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()


""" Colores utilizados según la leyenda de colores de la imagen, recuperado con IA de la imagen original
0 → (252, 240, 148)  Amarillo claro
1 → (0, 183, 239)    Azul cielo
2 → (113, 65, 36)    Café oscuro (tronquito)
3 → (248, 200, 37)   Amarillo abeja
4 → (107, 163, 194)  Azul medio
5 → (21, 22, 24)     Negro (rayas/ojos)
6 → (211, 241, 248)  Azul muy claro (alas/reflejo)
7 → (228, 173, 18)   Amarillo anaranjado
8 → (160, 213, 231)  Azul suave
9 → (206, 143, 75)   Café claro (miel)
"""


#Entonces se crea un diccionario que contenga la paleta de colores anteriormente mencionada, pero ya con clave hexadecimal
def get_color_map():
    return {
        0: "#fcf094",  # Amarillo claro
        1: "#00b7ef",  # Azul cielo
        2: "#714124",  # Café oscuro (tronquito)
        3: "#f8c825",  # Amarillo abeja
        4: "#6ba3c2",  # Azul medio
        5: "#151618",  # Negro (rayas/ojos)
        6: "#d3f1f8",  # Azul muy claro (alas/reflejo)
        7: "#e4ad12",  # Amarillo anaranjado
        8: "#a0d5e7",  # Azul suave
        9: "#ce8f4b",  # Café claro (miel)
    }




#Lectura del archivo . para ser interpretado (guardado en la matriz)
def cargar_matriz(nombre_archivo):                      #La función carga el archivo en una matriz 
    matriz = []                                         #Se crea un arreglo interno que guardará el contenido de los pixeles
    with open(nombre_archivo, newline="") as csvfile:   #Línea que busca el archivo y lo abre, el newline es como un enter o salto de renglón
        reader = csv.reader(csvfile)                    #Esto lee y revisa línea a línea el archivo del csv, lo guarda en tipo cadenas
        for fila in reader:                             #Se agregan los elementos a la lista
            matriz.append([int(x) for x in fila])       #Se insertan con el append
    return matriz                                       #Regresa el valor de la matriz guardada de las 100 columnas x 100 filas



#Una vez guardada la matriz en listas, el programa ya puede dibujar con turtle
def dibujar_matriz(matriz, pixel_size=6):               #Como la matriz es de 100 y la pantalla de 600, aquí podemos ajustarlo al tamaño
    filas = len(matriz)                                 #Da lectura a las filas de la matriz que guardamos
    columnas = len(matriz[0])                           #Da lectura a las columnas de la matriz que guardamos
    colores = get_color_map()                           #Obtiene el color según el diccionario con el mapa de colores


    # Configurar ventana
    t.setup(width=600, height=600)                      #Se configuran los valores exactos de la ventana emergente
    t.bgcolor("white")                                  #Se especifica que el tono de fondo sea blanco
    t.speed(0)                                          #Ajusta la velocidad de turtle para que sea más rápido
    t.hideturtle()                                      #Esconde el cursor de turtle para que no aparezca siempre
    t.tracer(0, 0)                                      #Este comando establece la modalidad turbo jaja que lo hace más rapidito
    start_x, start_y = -300, 300                        #Aquí ajustamos las coordenadas iniciales para empezar a pintar


#Este bucle crea poco a poco y fila a fila, la lectura de colores en la pantalla 
    for i in range(filas):
        for j in range(columnas):
            valor = matriz[i][j]
            color = colores.get(valor, "black")
            x = start_x + j * pixel_size
            y = start_y - i * pixel_size
            teleport(x, y)
            t.dot(pixel_size, color)  
        if i % 10 == 0:  
            t.update()


    t.update()
    t.done()

#Carga el programa principal, sin esta condición, no podría leer el archivo en csv que tenemos arriba y no podría iniciar 
if __name__ == "__main__":                                  #Detecta los archivos csv como el principal para poder cargar la matriz
    matriz = cargar_matriz("pixel_matrix_100x100.csv")      #Carga el archivo en formato csv
    dibujar_matriz(matriz, pixel_size=6)                    #Toma los anteriores parámetros e inicia la fase de dibujo
