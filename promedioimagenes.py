import tools as tl

# INSERTAR RUTA PARA GUARDAR IMÁGENES
path = rf"C:\Users\User\Desktop"
img_name = "apple"
img = tl.read_image(rf"{path}\{img_name}.jpg")

# Comparación de promedios.
sigma = 60
tl.comparacion_promedio_img(img_name,img,sigma,path)

# COMPARACIÓN PROMEDIO POR IMÁGEN DE 1 A cualquier número de 2 elevada a la n.
# 8 para 128
# 6 para 32
# 5 para 16
exponente = 6
tl.comparacion_grafica_ruido(img,img_name,path,sigma,exponente)

