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

##############################################################################

def imagem_media3(i,j,imagem):
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
    imagem = (sum(media) // len(media))
    
    return imagem

def imagem_media5(i, j, imagem):
    leste = imagem[i+1][j]
    oeste = imagem[i-1][j]
    norte = imagem[i][j-1]
    sul = imagem[i][j+1]
    centro = imagem[i][j]
    nordeste = imagem[i+1][j-1]
    noroeste = imagem[i-1][j-1]
    sudeste = imagem[i+1][j+1]
    sudoeste = imagem[i-1][j+1]
    leste5 = imagem[i+2][j]
    oeste5 = imagem[i-2][j]
    norte5 = imagem[i][j-2]
    sul5 = imagem[i][j+2]
    nordeste5 = imagem[i+2][j-2]
    noroeste5 = imagem[i-2][j-2]
    sudeste5 = imagem[i+2][j+2]
    sudoeste5 = imagem[i-2][j+2]
    media = [leste,oeste,norte,sul,centro,nordeste,noroeste,sudeste,sudoeste,leste5,oeste5,norte5,sul5,nordeste5,
             noroeste5,sudeste5,sudoeste5]
    imagem = (sum(media) // len(media))
    
    return imagem

def imagem_media7(i, j, imagem):
    leste = imagem[i+1][j]
    oeste = imagem[i-1][j]
    norte = imagem[i][j-1]
    sul = imagem[i][j+1]
    centro = imagem[i][j]
    nordeste = imagem[i+1][j-1]
    noroeste = imagem[i-1][j-1]
    sudeste = imagem[i+1][j+1]
    sudoeste = imagem[i-1][j+1]
    leste5 = imagem[i+2][j]
    oeste5 = imagem[i-2][j]
    norte5 = imagem[i][j-2]
    sul5 = imagem[i][j+2]
    nordeste5 = imagem[i+2][j-2]
    noroeste5 = imagem[i-2][j-2]
    sudeste5 = imagem[i+2][j+2]
    sudoeste5 = imagem[i-2][j+2]
    leste7 = imagem[i+3][j]
    oeste7 = imagem[i-3][j]
    norte7 = imagem[i][j-3]
    sul7 = imagem[i][j+3]
    nordeste7 = imagem[i+3][j-3]
    noroeste7 = imagem[i-3][j-3]
    sudeste7 = imagem[i+3][j+3]
    sudoeste7 = imagem[i-3][j+3]
    media = [leste,oeste,norte,sul,centro,nordeste,noroeste,sudeste,sudoeste,leste5,oeste5,norte5,sul5,
             nordeste5,noroeste5,sudeste5,sudoeste5,leste7,oeste7,norte7,sul7,nordeste7,noroeste7,sudeste7,sudoeste7]
    imagem = (sum(media) // len(media))
    
    return imagem

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
    img_array = array(img)
    img_arrayalt = array(img)
    
    if imgfilter == 'mean3':
        for i in range(len(img_array) -1):
            for j in range(len(img_array[i]) -1):
                img_arrayalt[i][j] = imagem_media3(i,j,img_array)
        new_image = Image.fromarray(img_arrayalt)
        
        imagem_media3(i, j, image)
        
    if imgfilter == 'mean5':
        for i in range(len(img_array) -2):
            for j in range(len(img_array[i]) -2):
                img_arrayalt[i][j] = imagem_media5(i,j,img_array)
        new_image = Image.fromarray(img_arrayalt)
        
        imagem_media5(i, j, image)

    if imgfilter == 'mean7':
        for i in range(len(img_array) -3):
            for j in range(len(img_array[i]) -3):
                img_arrayalt[i][j] = imagem_media7(i,j,img_array)
        new_image = Image.fromarray(img_arrayalt)
        
        imagem_media7(i, j, image)
        
    return new_image
    
mean3 = image_filter('mean3', img_array)
mean5 = image_filter('mean5', img_array)
mean7 = image_filter('mean7', img_array)
noise_white = image_noise('white', img)
noise_saltpepper = image_noise('salt_pepper', img)
noise_gaussian = image_noise('gaussian', img)

plt.figure(figsize = (30, 30))
plt.subplot(231)
plt.imshow(mean3)
plt.title('Mean 3')
plt.subplot(232)
plt.imshow(mean5)
plt.title('Mean 5')
plt.subplot(233)
plt.imshow(mean7)
plt.title('Mean 7')
# plt.subplot(234)
# plt.hist(array(mean3).ravel())
# plt.title('mean3 hist')
# plt.subplot(235)
# plt.hist(array(mean5).ravel())
# plt.title('mean5 hist')
# plt.subplot(236)
# plt.hist(array(mean7).ravel())
# plt.title('mean7 hist')
plt.subplot(234)
plt.imshow(noise_white)
plt.title('White Noise')
plt.subplot(235)
plt.imshow(noise_saltpepper)
plt.title('Salt and Pepper Noise')
plt.subplot(236)
plt.imshow(noise_gaussian)
plt.title('Gaussian Noise')