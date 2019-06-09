from PIL import Image
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
import numpy as np

img = Image.open('images/Lenna.png').convert('L')
img_array = array(img)
img_array1 = array(img)  # noise
img_array2 = array(img)  # noise
img_array3 = array(img)  # noise
img_arrayalt = array(img)

def image_noise(noise, image):
    ''' noise é o tipo de ruído que será introduzido na imagem, podendo ser:
        - salt_and_pepper
        - white
        - gaussian
    '''
    new_image = image
    if noise == 'white':
        for i in range(len(new_image)):
            for j in range(len(new_image[i])):
                random = randint(0, (len(new_image) -1))
                random_j = randint(0, (len(new_image[i]) -1))
                new_image[random][random_j] = 255
            
    if noise == 'salt_pepper':
        for i in range(len(new_image)):
            for j in range(len(new_image)):
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
        random = np.random.randn(len(new_image), len(new_image))
        for i in range(0, len(new_image)):
            aux = new_image[i]
            for j in range(0, len(aux)):
                valor = aux[j] + (random[i][j] * gama)
                aux[j] = valor
    
    return new_image

##############################################################################

def imagem_media3(i, j, imagem):
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
    nordeste5lado = imagem[i+2][j-1]
    noroeste5lado = imagem[i-2][j-1]
    norte5esq = imagem[i-1][j-2]
    norte5dir = imagem[i+1][j-2]
    sudeste5lado = imagem[i+2][j+1]
    sudoeste5lado = imagem[i-2][j-1]
    sul5esq = imagem[i-1][j+2]
    sul5dir = imagem[i+1][j+2]
    media = [leste,oeste,norte,sul,centro,nordeste,noroeste,sudeste,sudoeste,
             leste5,oeste5,norte5,sul5,nordeste5,noroeste5,sudeste5,sudoeste5,
             nordeste5lado,noroeste5lado,norte5esq,norte5dir,sudeste5lado,sudoeste5lado,
             sul5esq,sul5dir]
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
    nordeste5lado = imagem[i+2][j-1]
    noroeste5lado = imagem[i-2][j-1]
    norte5esq = imagem[i-1][j-2]
    norte5dir = imagem[i+1][j-2]
    sudeste5lado = imagem[i+2][j+1]
    sudoeste5lado = imagem[i-2][j-1]
    sul5esq = imagem[i-1][j+2]
    sul5dir = imagem[i+1][j+2]
    leste7 = imagem[i+3][j]
    oeste7 = imagem[i-3][j]
    norte7 = imagem[i][j-3]
    sul7 = imagem[i][j+3]
    nordeste7 = imagem[i+3][j-3]
    noroeste7 = imagem[i-3][j-3]
    sudeste7 = imagem[i+3][j+3]
    sudoeste7 = imagem[i-3][j+3]
    leste7cima = imagem[i+3][j-1]
    leste7baixo = imagem[i+3][j+1]
    oeste7cima = imagem[i-3][j-1]
    oeste7baixo = imagem[i-3][j+1]
    nordeste7lado = imagem[i+3][j-2]
    sudeste7lado = imagem[i+3][j+2]
    noroeste7lado = imagem[i-3][j-2]
    sudoeste7lado = imagem[i-3][j+2]
    norte7dir1 = imagem[i+1][j-3]
    norte7dir2 = imagem[i+2][j-3]
    norte7esq1 = imagem[i-1][j-3]
    norte7esq2 = imagem[i-2][j-3]
    sul7dir1 = imagem[i+1][j+3]
    sul7dir2 = imagem[i+2][j+3]
    sul7esq1 = imagem[i-1][j+3]
    sul7esq2 = imagem[i-2][j+3]
    media = [leste,oeste,norte,sul,centro,nordeste,noroeste,sudeste,sudoeste,
             leste5,oeste5,norte5,sul5,nordeste5,noroeste5,sudeste5,sudoeste5,
             nordeste5lado,noroeste5lado,norte5esq,norte5dir,sudeste5lado,sudoeste5lado,
             sul5esq,sul5dir,leste7,oeste7,norte7,sul7,nordeste7,noroeste7,sudeste7,
             sudoeste7,leste7cima,leste7baixo,oeste7cima,oeste7baixo,nordeste7lado,
             sudeste7lado,noroeste7lado,sudoeste7lado,norte7dir1,norte7dir2,
             norte7esq1,norte7esq2,sul7dir1,sul7dir2,sul7esq1,sul7esq2]
    imagem = (sum(media) // len(media))
    
    return imagem

def imagem_mediana(imagem):
    for i in range (len(imagem)-1):
        for j in range (len(imagem[i])-1):
            leste = imagem[i+1][j]
            oeste = imagem[i-1][j]
            norte = imagem[i][j-1]
            sul = imagem[i][j+1]
            centro = imagem[i][j]
            nordeste = imagem[i+1][j-1]
            noroeste = imagem[i-1][j-1]
            sudeste = imagem[i+1][j+1]
            sudoeste = imagem[i-1][j+1]
            mediana = [leste,oeste,norte,sul,centro,nordeste,noroeste,sudeste,sudoeste]
            mediana.sort()            
            img_arrayalt[i][j] = mediana[4]
    imagem = Image.fromarray(img_arrayalt)
    return imagem

def imagem_gaussian3(i, j, imagem):
    leste = (imagem[i+1][j] * 0.13)
    oeste = (imagem[i-1][j] * 0.13)
    norte = (imagem[i][j-1] * 0.13)
    sul = (imagem[i][j+1] * 0.13)
    centro = (imagem[i][j] * 0.2)
    nordeste = (imagem[i+1][j-1] * 0.06)
    noroeste = (imagem[i-1][j-1] * 0.06)
    sudeste = (imagem[i+1][j+1] * 0.06)
    sudoeste = (imagem[i-1][j+1] * 0.06)
    media = [leste,oeste,norte,sul,centro,nordeste,noroeste,sudeste,sudoeste]
    imagem = (sum(media))
    # imagem = (sum(media) // len(media))
    
    return imagem

def imagem_gaussian5(i, j, imagem):
    leste = (imagem[i+1][j] * 0.26)
    oeste = (imagem[i-1][j] * 0.26)
    norte = (imagem[i][j-1] * 0.26)
    sul = (imagem[i][j+1] * 0.26)
    centro = (imagem[i][j] * 0.4)
    nordeste = (imagem[i+1][j-1] * 0.12)
    noroeste = (imagem[i-1][j-1] * 0.12)
    sudeste = (imagem[i+1][j+1] * 0.12)
    sudoeste = (imagem[i-1][j+1] * 0.12)
    leste5 = (imagem[i+2][j] * 0.06)
    oeste5 = (imagem[i-2][j] * 0.06)
    norte5 = (imagem[i][j-2] * 0.06)
    sul5 = (imagem[i][j+2] * 0.06)
    nordeste5 = (imagem[i+2][j-2] * 0.01)
    noroeste5 = (imagem[i-2][j-2] * 0.01)
    sudeste5 = (imagem[i+2][j+2] * 0.01)
    sudoeste5 = (imagem[i-2][j+2] * 0.01)
    nordeste5lado = (imagem[i+2][j-1] * 0.03)
    noroeste5lado = (imagem[i-2][j-1] * 0.03)
    norte5esq = (imagem[i-1][j-2] * 0.03)
    norte5dir = (imagem[i+1][j-2] * 0.03)
    sudeste5lado = (imagem[i+2][j+1] * 0.03)
    sudoeste5lado = (imagem[i-2][j-1] * 0.03)
    sul5esq = (imagem[i-1][j+2] * 0.03)
    sul5dir = (imagem[i+1][j+2] * 0.03)
    media = [leste,oeste,norte,sul,centro,nordeste,noroeste,sudeste,sudoeste,
             leste5,oeste5,norte5,sul5,nordeste5,noroeste5,sudeste5,sudoeste5,
             nordeste5lado,noroeste5lado,norte5esq,norte5dir,sudeste5lado,sudoeste5lado,
             sul5esq,sul5dir]
    imagem = (sum(media))
    # imagem = (sum(media) // len(media))
    
    return imagem

def imagem_gaussian7(i, j, imagem):
    leste = (imagem[i+1][j] * 0.52)
    oeste = (imagem[i-1][j] * 0.52)
    norte = (imagem[i][j-1] * 0.52)
    sul = (imagem[i][j+1] * 0.52)
    centro = (imagem[i][j] * 0.8)
    nordeste = (imagem[i+1][j-1] * 0.24)
    noroeste = (imagem[i-1][j-1] * 0.24)
    sudeste = (imagem[i+1][j+1] * 0.24)
    sudoeste = (imagem[i-1][j+1] * 0.24)
    leste5 = (imagem[i+2][j] * 0.12)
    oeste5 = (imagem[i-2][j] * 0.12)
    norte5 = (imagem[i][j-2] * 0.12)
    sul5 = (imagem[i][j+2] * 0.12)
    nordeste5 = (imagem[i+2][j-2] * 0.06)
    noroeste5 = (imagem[i-2][j-2] * 0.06)
    sudeste5 = (imagem[i+2][j+2] * 0.06)
    sudoeste5 = (imagem[i-2][j+2] * 0.06)
    nordeste5lado = (imagem[i+2][j-1] * 0.06)
    noroeste5lado = (imagem[i-2][j-1] * 0.06)
    norte5esq = (imagem[i-1][j-2] * 0.06)
    norte5dir = (imagem[i+1][j-2] * 0.06)
    sudeste5lado = (imagem[i+2][j+1] * 0.06)
    sudoeste5lado = (imagem[i-2][j-1] * 0.06)
    sul5esq = (imagem[i-1][j+2] * 0.06)
    sul5dir = (imagem[i+1][j+2] * 0.06)
    leste7 = (imagem[i+3][j] * 0.06)
    oeste7 = (imagem[i-3][j] * 0.06)
    norte7 = (imagem[i][j-3] * 0.06)
    sul7 = (imagem[i][j+3] * 0.06)
    nordeste7 = (imagem[i+3][j-3] * 0.01)
    noroeste7 = (imagem[i-3][j-3] * 0.01)
    sudeste7 = (imagem[i+3][j+3] * 0.01)
    sudoeste7 = (imagem[i-3][j+3] * 0.01)
    leste7cima = (imagem[i+3][j-1] * 0.03)
    leste7baixo = (imagem[i+3][j+1] * 0.03)
    oeste7cima = (imagem[i-3][j-1] * 0.03)
    oeste7baixo = (imagem[i-3][j+1] * 0.03)
    nordeste7lado = (imagem[i+3][j-2] * 0.03)
    sudeste7lado = (imagem[i+3][j+2] * 0.03)
    noroeste7lado = (imagem[i-3][j-2] * 0.03)
    sudoeste7lado = (imagem[i-3][j+2] * 0.03)
    norte7dir1 = (imagem[i+1][j-3] * 0.03)
    norte7dir2 = (imagem[i+2][j-3] * 0.03)
    norte7esq1 = (imagem[i-1][j-3] * 0.03)
    norte7esq2 = (imagem[i-2][j-3] * 0.03)
    sul7dir1 = (imagem[i+1][j+3] * 0.03)
    sul7dir2 = (imagem[i+2][j+3] * 0.03)
    sul7esq1 = (imagem[i-1][j+3] * 0.03)
    sul7esq2 = (imagem[i-2][j+3] * 0.03)
    media = [leste,oeste,norte,sul,centro,nordeste,noroeste,sudeste,sudoeste,
             leste5,oeste5,norte5,sul5,nordeste5,noroeste5,sudeste5,sudoeste5,
             nordeste5lado,noroeste5lado,norte5esq,norte5dir,sudeste5lado,sudoeste5lado,
             sul5esq,sul5dir,leste7,oeste7,norte7,sul7,nordeste7,noroeste7,sudeste7,
             sudoeste7,leste7cima,leste7baixo,oeste7cima,oeste7baixo,nordeste7lado,
             sudeste7lado,noroeste7lado,sudoeste7lado,norte7dir1,norte7dir2,
             norte7esq1,norte7esq2,sul7dir1,sul7dir2,sul7esq1,sul7esq2]
    imagem = (sum(media))
    # imagem = (sum(media) // len(media))
    
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
        - prewitt
        - sobel
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
        
    if imgfilter == 'mediana':
        new_image = imagem_mediana(image)
        
    if imgfilter == 'gaussian3':
        for i in range(len(img_array) -1):
            for j in range(len(img_array[i]) -1):
                img_arrayalt[i][j] = imagem_gaussian3(i,j,img_array)
        new_image = Image.fromarray(img_arrayalt)
        
        imagem_gaussian3(i, j, image)
        
    if imgfilter == 'gaussian5':
        for i in range(len(img_array) -2):
            for j in range(len(img_array[i]) -2):
                img_arrayalt[i][j] = imagem_gaussian5(i,j,img_array)
        new_image = Image.fromarray(img_arrayalt)
        
        imagem_gaussian5(i, j, image)
        
    if imgfilter == 'gaussian7':
        for i in range(len(img_array) -3):
            for j in range(len(img_array[i]) -3):
                img_arrayalt[i][j] = imagem_gaussian7(i,j,img_array)
        new_image = Image.fromarray(img_arrayalt)
        
        imagem_gaussian7(i, j, image)
        
    if imgfilter == 'prewitt':
        img_array = array(img)
        mediax = array(img)
        img_novo = array(img)
        lst_vizinhosx = []
        for i in range (len(img_array)):
            for j in range (len(img_array[i])):
                meio = 0
                try:
                    lst_vizinhosx.append(img_array[i][j]*0)
                    lst_vizinhosx.append(img_array[i][j-1]*-1) #esquerda
                    lst_vizinhosx.append(img_array[i][j+1]*1) #direita
                    lst_vizinhosx.append(img_array[i-1][j]*0) #cima
                    lst_vizinhosx.append(img_array[i+1][j]*0) #baixo
                    lst_vizinhosx.append(img_array[i-1][j-1]*-1) #canto superior esquerdo
                    lst_vizinhosx.append(img_array[i-1][j+1]*1) #canto superior direito
                    lst_vizinhosx.append(img_array[i+1][j-1]*-1) #canto inferior esquerdo
                    lst_vizinhosx.append(img_array[i+1][j+1]*1) #canto inferior direito
                except:
                    pass
                mediax[i][j] = sum(lst_vizinhosx) // len(lst_vizinhosx)
                del lst_vizinhosx[:]
                
        mediay = array(img)
        lst_vizinhosy = []
        for i in range (len(img_array)):
            for j in range (len(img_array[i])):
                meio = 0
                try:
                    lst_vizinhosy.append(img_array[i][j]*0)
                    lst_vizinhosy.append(img_array[i][j-1]*0) #esquerda
                    lst_vizinhosy.append(img_array[i][j+1]*0) #direita
                    lst_vizinhosy.append(img_array[i-1][j]*-1) #cima
                    lst_vizinhosy.append(img_array[i+1][j]*1) #baixo
                    lst_vizinhosy.append(img_array[i-1][j-1]*-1) #canto superior esquerdo
                    lst_vizinhosy.append(img_array[i-1][j+1]*-1) #canto superior direito
                    lst_vizinhosy.append(img_array[i+1][j-1]*1) #canto inferior esquerdo
                    lst_vizinhosy.append(img_array[i+1][j+1]*1) #canto inferior direito

                except:
                    pass
                mediay[i][j] = sum(lst_vizinhosy) // len(lst_vizinhosy)
                del lst_vizinhosy[:]

        for i in range (len(img_array)):
            for j in range (len(img_array[i])):
                img_novo[i][j] = int(mediay[i][j]) + int(mediax[i][j])
        
        new_image = Image.fromarray(img_novo)
    
    if imgfilter == 'sobel':
        img_array = array(img)
        mediax = array(img)
        img_novo = array(img)
        lst_vizinhosx = []
        for i in range (len(img_array)):
            for j in range (len(img_array[0])):
                meio = 0
                try:
                    lst_vizinhosx.append(img_array[i][j]*0)
                    lst_vizinhosx.append(img_array[i][j-1]*-2) #esquerda
                    lst_vizinhosx.append(img_array[i][j+1]*2) #direita
                    lst_vizinhosx.append(img_array[i-1][j]*0) #cima
                    lst_vizinhosx.append(img_array[i+1][j]*0) #baixo
                    lst_vizinhosx.append(img_array[i-1][j-1]*-1) #canto superior esquerdo
                    lst_vizinhosx.append(img_array[i-1][j+1]*1) #canto superior direito
                    lst_vizinhosx.append(img_array[i+1][j-1]*-1) #canto inferior esquerdo
                    lst_vizinhosx.append(img_array[i+1][j+1]*1) #canto inferior direito
                except:
                    pass
                mediax[i][j] = sum(lst_vizinhosx) // len(lst_vizinhosx)
                del lst_vizinhosx[:]

        mediay = array(img)
        lst_vizinhosy = []
        for i in range (len(img_array)):
            for j in range (len(img_array[i])):
                meio = 0
                try:
                    lst_vizinhosy.append(img_array[i][j]*0)
                    lst_vizinhosy.append(img_array[i][j-1]*0) #esquerda
                    lst_vizinhosy.append(img_array[i][j+1]*0) #direita
                    lst_vizinhosy.append(img_array[i-1][j]*-2) #cima
                    lst_vizinhosy.append(img_array[i+1][j]*2) #baixo
                    lst_vizinhosy.append(img_array[i-1][j-1]*-1) #canto superior esquerdo
                    lst_vizinhosy.append(img_array[i-1][j+1]*-1) #canto superior direito
                    lst_vizinhosy.append(img_array[i+1][j-1]*1) #canto inferior esquerdo
                    lst_vizinhosy.append(img_array[i+1][j+1]*1) #canto inferior direito
                except:
                    pass
                mediay[i][j] = sum(lst_vizinhosy) // len(lst_vizinhosy)
                del lst_vizinhosy[:]

        for i in range (len(img_array)):
            for j in range (len(img_array[i])):
                img_novo[i][j] = int(mediay[i][j]) + int(mediax[i][j])
    
        new_image = Image.fromarray(img_novo)
    
    return new_image
    
mean3 = image_filter('mean3', img_array)
mean5 = image_filter('mean5', img_array)
mean7 = image_filter('mean7', img_array)
mediana = image_filter('mediana', img_array)
gaussian3 = image_filter('gaussian3', img_array)
gaussian5 = image_filter('gaussian5', img_array)
gaussian7 = image_filter('gaussian7', img_array)
prewitt = image_filter('prewitt', img_array)
sobel = image_filter('sobel', img_array)

image_noise('white', img_array1)
noise_white = Image.fromarray(img_array1)
image_noise('salt_pepper', img_array2)
noise_saltpepper = Image.fromarray(img_array2)
image_noise('gaussian', img_array3)
noise_gaussian = Image.fromarray(img_array3)

plt.figure(figsize = (30, 30))
plt.subplot(431)
plt.imshow(noise_white)
plt.title('White Noise')
plt.subplot(432)
plt.imshow(noise_saltpepper)
plt.title('Salt and Pepper Noise')
plt.subplot(433)
plt.imshow(noise_gaussian)
plt.title('Gaussian Noise')
plt.subplot(434)
plt.imshow(mean3)
plt.title('Mean 3')
plt.subplot(435)
plt.imshow(mean5)
plt.title('Mean 5')
plt.subplot(436)
plt.imshow(mean7)
plt.title('Mean 7')
plt.subplot(437)
plt.imshow(gaussian3)
plt.title('Gaussian 3')
plt.subplot(438)
plt.imshow(gaussian5)
plt.title('Gaussian 5')
plt.subplot(439)
plt.imshow(gaussian7)
plt.title('Gaussian 7')
plt.subplot(4,3,10)
plt.imshow(mediana)
plt.title('Mediana')
plt.subplot(4,3,11)
plt.imshow(prewitt)
plt.title('Prewitt')
plt.subplot(4,3,12)
plt.imshow(sobel)
plt.title('Sobel')