from skimage.color import rgb2gray
from skimage.io import imread
import numpy as np
import matplotlib.pyplot as plt

# FUNCIÓN LEER IMÁGENES
def read_image(image_path):
    img = imread(image_path)
    if len(img.shape) == 3:
        img = rgb2gray(img)
        img = (img * 255).astype(np.float32)
    else:
        img = img.astype(np.float32)
    return img

# FUNCIÓN PARA SUMAR RUIDO QUE NO RETORNE IMAGEN DE RUIDO
def suma_ruido(img, sigma):
    w,h = img.shape
    img_ruido = np.random.normal(0,sigma,(w,h))
    img_out = img + img_ruido
    return img_out

# FUNCION PROMEDIO RUIDO DE UNA IMAGEN
def promedio_ruido_img(img,n,sigma):
    imagenes_ruidosas = []
    w,h = img.shape
    img_out = np.zeros((w,h))
    img_suma = np.zeros((w,h))
    for i in range(n):
        img_out = suma_ruido(img,sigma)
        imagenes_ruidosas.append(img_out)
        for j in range(w):
            for k in range(h):
                img_suma[j][k] += imagenes_ruidosas[i][j][k]

    img_promedio = img_suma / n

    return img_promedio

# FUNCION PROMEDIO RUIDO DE UNA RUIDO
def promedio_ruido_ruido(w,h,n,sigma):
    imagenes_ruidosas = []
    img_ruido = np.random.normal(0,sigma,(w,h))
    img_suma = np.zeros((w,h))
    for i in range(n):
        imagenes_ruidosas.append(img_ruido)
        for j in range(w):
            for k in range(h):
                img_suma[j][k] += imagenes_ruidosas[i][j][k]

    img_promedio = img_suma / n

    return img_promedio

# Creación de una imágen promedio y exportación para comparación
def comparacion_promedio_img(img_name, img,sigma,path):
    lista_exponentes = [2,4,8,16,32,64,128,256]
    lista_promedios = []
    for i in lista_exponentes:
        imgs = promedio_ruido_img(img,i+1,sigma)
        lista_promedios.append(imgs)
    fig, axs = plt.subplots(2, 4, figsize=(12, 6))
    fig.suptitle(f"Comparación ruido de 256 imágenes sigma de {sigma}")
    for i in range(len(lista_exponentes)):
        ax = axs[i // 4, i % 4]
        ax.imshow(lista_promedios[i], cmap="gray")
        ax.axis("off")
        ax.set_title(f"Ruido con {lista_exponentes[i]} imgs")
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)
    plt.savefig(rf"{path}\{img_name}_ruido_sigma{sigma}.png")

# Comparación de ruido de una imagen de 1 a 64
def comparacion_promedio_ruido_img_dinamica(img,img_name,path,sigma,bit):
    lista_exponentes = []
    for i in range(bit):
        lista_exponentes.append(2**i)
    lista_promedios = []
    img_original = img.sum()
    lista_promedios.append(img_original)
    for i in lista_exponentes:
        imgs = promedio_ruido_img(img,i+1,sigma)
        imgsum = imgs.sum()
        lista_promedios.append(imgsum)
    fig, ax = plt.subplots()
    lista_nueva =[0]
    for i in range(bit):
        lista_nueva.append(lista_exponentes[i])
    ax.plot(lista_nueva, lista_promedios)
    ax.set_title(f"Comparación ruido de {img_name} {lista_exponentes[len(lista_exponentes) - 1]} imágenes de sigma {sigma}.png")
    plt.title(f"Ruido de {img_name} 1 a {lista_exponentes[len(lista_exponentes) - 1]} imagenes")
    plt.savefig(rf"{path}\comparacion{bit}_ruido_{img_name}_sigma_{sigma}.png")
    plt.show()

# Creación de una imágen promedio y exportación para comparación
def comparacion_grafica_ruido(img, img_name,path,sigma,bit):
    labels = [0]
    lista_exponentes = []
    plt.figure()
    for i in range(bit):
            lista_exponentes.append(2**i)
    lista_nueva =[0]
    for i in range(bit):
        lista_nueva.append(lista_exponentes[i])
    for j in range(bit):
        labels.append(f"Iteracion {j}")
    for j in range(bit):
        lista_promedios = []
        img_original = img.sum()
        lista_promedios.append(img_original)
        for i in lista_exponentes:
            imgs = promedio_ruido_img(img,i+1,sigma)
            imgsum = imgs.sum()
            lista_promedios.append(imgsum)
        plt.plot(lista_nueva,lista_promedios, label=labels)
    plt.title(f"Comparación ruido de {img_name} 1 a {lista_exponentes[len(lista_exponentes) - 1]} imagenes de sigma {sigma}")
    plt.savefig(rf"{path}\comparacion{bit}_ruido_{img_name}_sigma_{sigma}.png")
    plt.show()