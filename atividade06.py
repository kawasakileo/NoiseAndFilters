from PIL import Image
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
import numpy as np

img = Image.open('images/Lenna.png').convert('L')
img_array = array(img)
img_arrayalt = array(img)

def image_noise(noise, image):
    ''' noise é o tipo de ruído que será introduzido na imagem, podendo ser:
        - salt_and_pepper
        - white
        - gaussian
    '''
    new_image = array(image)
    if noise == 'white':
        for i in range(len(new_image)):
            random = randint(0, (len(new_image) -1))
            random_j = randint(0, (len(new_image[i]) -1))
            new_image[random][random_j] = 255
            
    if noise == 'salt_pepper':
        for i in range(len(new_image)):
            random = randint(0, (len(new_image) -1))
            random_j = randint(0, (len(new_image[i]) -1)) 
            cor = randint(0, 2)
            if cor == 0:
                new_image[random][random_j] = 0
            else:
                new_image[random][random_j] = 255
    
    if noise == 'gaussian':
        valor = 0
        gama = 50
        random = np.random.randn(len(new_image),len(new_image))
        for i in range(0, len(new_image)):
            aux = new_image[i]
            for j in range(0, len(aux)):
                valor = aux[j] + (random[i][j] * gama)
                aux[j] = valor
        
    Image.fromarray(new_image)
    
    return new_image

def imagem_mediaD4(i, j, imagem):
    leste = imagem[i+1][j]
    oeste = imagem[i-1][j]
    norte = imagem[i][j-1]
    sul = imagem[i][j+1]
    centro = imagem[i][j]
    media = [leste,oeste,norte,sul,centro]
    imagem = (sum(media) / len(media))
    
    return imagem

for i in range(len(img_array) -1):
    for j in range(len(img_array[i]) -1):
        img_arrayalt[i][j] = imagem_mediaD4(i,j,img_array)
new_image = Image.fromarray(img_arrayalt)

def imagem_mediaD8(i,j,imagem):
    leste = imagem[i+1][j]
    oeste = imagem[i-1][j]
    norte = imagem[i][j-1]
    sul = imagem[i][j+1]
    centro = imagem[i][j]
    nordeste = imagem[i+1][j-1]
    noroeste = imagem[i-1][j-1]
    sudeste = imagem[i+1][j+1]
    sudoeste = imagem[i-1][j+1]
    media = [leste,oeste,norte,sul,centro,nordeste,noroeste,sudeste,sudoeste]
    imagem = (sum(media) / len(media))
    
    return imagem

for i in range(len(img_array) -1):
    for j in range(len(img_array[i]) -1):
        img_arrayalt[i][j] = imagem_mediaD8(i,j,img_array)
imagemD8 = Image.fromarray(img_arrayalt)


def image_filter(imgfilter, image):
    ''' Os seguintes filtros deverão ser implementados:
        - mediana
        - gaussiano3
        - gaussiano5
        - gaussiano7
        - mean3
        - mean5
        - mean7
    '''
    if imgfilter == 'mean3_d4':
        imagem_mediaD4(i, j, image)
    if imgfilter == 'mean3_d8':
        imagem_mediaD8(i, j, image)
        
    return new_image;

mean3_d4 = image_filter('mean3_d4', img_array)
mean3_d8 = image_filter('mean3_d8', img_array)
noise_white = image_noise('white', img)
noise_saltpepper = image_noise('salt_pepper', img)
noise_gaussian = image_noise('gaussian', img)

plt.figure(figsize = (15, 15))
plt.subplot(231)
plt.imshow(mean3_d4)
plt.title('Mean 3 - D4')
plt.subplot(232)
plt.imshow(mean3_d8)
plt.title('Mean 3 - D8')
plt.subplot(234)
plt.imshow(noise_white)
plt.title('White Noise')
plt.subplot(235)
plt.imshow(noise_saltpepper)
plt.title('Salt and Pepper Noise')
plt.subplot(236)
plt.imshow(noise_gaussian)
plt.title('Gaussian Noise')