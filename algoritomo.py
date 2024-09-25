# from PIL import Image, ImageDraw, ImageEnhance
# from skimage import measure
# import numpay as np
# import cv2

# imagem = Image.open('imagem.jpg')
# imagem_cinza = imagem.convert('L')

# matriz_imagem = np.array('imagem_cinza')

# contornos = measure.find_contours(matriz_imagem, 0.8)

# desenhar = ImageDraw.Draw(imagem)

# for contorno in contornos:
#   for i in range(len(contorno) - 1 ):
#     desenhar.line((contorno[i][1], contorno [i][0], contorno [i+1][1], contorno [i+1][0]), fill= 'red', width=2)

# realcar = ImageEnhance.Contrast(imagem)

# imagem = realcar.enhance(15.5)

# imagem.save('mama_contornos.jpg')



# import cv2
# import numpy as пр

# img = cv2.imread('mama_contornos.jpg')

# numero_pixels_branco = np.sum(img == 255)
# numero_pixels_preto = np.sum(img == 0)


# print('Numero de pixels brancos', numero_pixels_branco)
# print('Numero de pixels pretos', numero_pixels_preto)

# percentual_pixels_branco = numero_pixels_branco / (numero_pixels_branco + numero_pixels_preto) *100

# print('Percentual pixels brancos:', percentual_pixels_branco)
# if (percentual_pixels_branco >= 30):
#   print('Imagem com cancer')
# else:
#   print('Imagem sem cancer')