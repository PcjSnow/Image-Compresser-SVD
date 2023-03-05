#Autor: PcjSnow


from PIL import Image
import numpy as np
import os

def positive_eigenvalues(eigenvalues_ordenados):
    positivos = []

    for eigenvalue in eigenvalues_ordenados:

        if eigenvalue >= 0:
            positivos.append(eigenvalue)
        
    return positivos

def singular_values(eingenvalues_positivos):
    singular = []

    for eigenvalue in eigenvalues_positivos:
        singular.append(np.sqrt(eigenvalue))

    return singular

def comprimirImagen( U, S, V, k, filas, columnas):

    matriz_comprimida = np.zeros((filas, columnas))
    
    for i in range (0, k):
        
        #aquí estamos usando la forma de producto exterior de la DVS
        matriz_comprimida += S[i] * np.dot(((U[:, i]).reshape(-1,1)), ((V[i, :]).reshape(1, -1)))

    return matriz_comprimida



nombreImagen = input("Nombre de la imagen a comprimir: ")
imagenOriginal = Image.open(nombreImagen)
#La convertimos en una imagen en blanco y negro, para que la matriz sea 2-dimensional.

imagen = imagenOriginal.convert('L')
ancho, altura = imagen.size
pixelsize = ancho*altura;

tamagno_original = os.path.getsize("./"+nombreImagen)

#La convertimos en una matriz de 2 dimensiones de tamaño altura x anchura
matriz = np.array(imagen)
#Hallamos su traspuesta
traspuesta = matriz.transpose()
#Y su producto, el cual es simétrico, para hallar los eigenvalores
producto = np.dot(traspuesta, matriz)
eigenvalues = np.linalg.eigvals(producto);
print("Hay", len(eigenvalues), "eigenvalues")

eigenvalues_ordenados = sorted(eigenvalues, reverse=True)

eigenvalues_positivos = positive_eigenvalues(eigenvalues_ordenados)
print("Hay ", len(eigenvalues_positivos), "eigenvalues positivos")

#Vamos a hallar la descomposición en valores singulares (DVS) de matriz 
U, S, V = np.linalg.svd(matriz)
print("Hay un total de ", len(S)," valores singulares. ¿Cuántos deseas usar para aproximar la imagen? (cuantos más se usen más fiel será a la imagen original): ")

k = int(input())
#La forma de producto exterior de la DVS nos dice que "matriz" = σ_1*u_1*(v_1)^T + σ_2*u_2*(v_2)^T + ... + σ_r*u_r*(v_r)^T, σ_1 >= σ_2 >= ... >= σ_r > 0
#siendo σ_i el i-esimo valor singular de "matriz", u_i y v_i las i-ésimas columnas de U y V respectivamente y r el número de valores singulares.

matriz_comprimida = comprimirImagen(U, S, V, k, altura, ancho)

#debemos convertir la matriz comprimida en una cuyas entradas sean enteros del tipo unsigned int de 8 bits, pues es lo que necesita
#la función Image.fromarray() para leer en modo "L" (escala de grises)
matriz_comprimida_entera = np.floor(matriz_comprimida).astype(np.uint8)


img = Image.fromarray(matriz_comprimida_entera, mode="L")

nombreFinal = input("¿Cómo deseas llamar (con extensión) a la imagen comprimida?: ")
img.save(nombreFinal)
print("El tamaño original era de ", tamagno_original, "bytes.")
tamagno_comprimido = os.path.getsize("./"+nombreFinal)
print("La imagen comprimida pesa ", tamagno_comprimido, "bytes.")

print("La tasa de compresión es del ", round((tamagno_comprimido/tamagno_original*100), 2), "%.")
