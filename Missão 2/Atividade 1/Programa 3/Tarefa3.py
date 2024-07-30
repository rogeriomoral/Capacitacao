import cv2
import os
import numpy as np

# Função para mostrar as imagens
def displayImagem(nomeJanela1, imagem1, nomeJanela2, imagem2):
    cv2.imshow(nomeJanela1, imagem1) #Mostra a imagem 1
    cv2.imshow(nomeJanela2, imagem2) #mostrar imagem 2
    cv2.waitKey(0) #Espera pressionar uma tecla
    cv2.destroyAllWindows()

def reScaling(imagem, fatorEscala):
    altura, largura, canais = imagem.shape

    novaAltura = int(altura * fatorEscala)
    novaLargura = int(largura * fatorEscala)
    novaDimensao = (novaLargura, novaAltura)

    return cv2.resize(imagem, novaDimensao, interpolation=cv2.INTER_AREA)

def configurarBrilho(imagem, alpha, beta):
    # beta é o valor para ajuste de brilho, se positivo o brilho aumenta, se negativo o brilho diminui
    # alpha é a intensidade
    return cv2.convertScaleAbs(imagem, alpha=alpha, beta=beta)

# i. Blurring por Convolução: aplica uma matriz sobre a imagem
def blurringConvolucao(imagem):

    kernel = np.ones((5, 5), np.float32) / 30
    return cv2.filter2D(imagem, -1, kernel)

# ii. Regular Blurring
def regularBlurring(imagem):
    return cv2.blur(imagem, (15,15))

# iii. Gaussian Blurring
def gaussianBlurring(imagem):
    return cv2.GaussianBlur(imagem, (15,15), 0)

# i. Regular Thresholding: usa um unico valor limiar para todos os pixels
# bom para imagens sem mt variação de iluminação
def regularThreshold(imagem):
    imgGray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    # 127: valor do limiar
    # 255: valor max dos pixels que excedem o limiar
    # pixels acima de 127 são brancos, pixels com valores abaixo de 127 são pretos
    _, thresh =  cv2.threshold(imgGray, 127, 255, cv2.THRESH_BINARY)
    return thresh

# ii. Adaptive Thresholding: calcula o limiar localmente para diferentes regiões da imagem
# bom para imagens com variações de iluminação
def adaptiveThreshold(imagem):
    imgGray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    # ADAPTIVE_THRESH_MEAN_C: usa a média dos valores dos pixels vizinhos
    # 11: tamanho da área vizinha
    # 2: constante subtraida da média
    return cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)



def main():
    os.chdir(r"D:\download v2\ras capacitação\Capacitacao\Missão 2\Atividade 1\imagens")
    imagem = cv2.imread("imagemSalva.jpg")

    #re-scaling 
    imagemRedimensionada = reScaling(imagem, 0.5)
    displayImagem('imagem original', imagem, 'imagem redimensionada', imagemRedimensionada)


    #brilho
    imgBrilhoAumentado = configurarBrilho(imagem, 1, 50)
    imgBrilhoDiminuido = configurarBrilho(imagem, 1, -50)
    displayImagem('brilho aumentado', imgBrilhoAumentado, 'brilho diminuido', imgBrilhoDiminuido)


    #blur
    imgBlurConvolucao = blurringConvolucao(imagem)
    displayImagem('imagem original', imagem, 'blur convolucao', imgBlurConvolucao)

    imgRegularBlur = regularBlurring(imagem)
    displayImagem('imagem original', imagem, 'regular blur', imgRegularBlur)

    imgGaussianBlur = gaussianBlurring(imagem)
    displayImagem('imagem original', imagem, 'gaussian blur', imgGaussianBlur)


    # thresholding
    imgRegularThresh = regularThreshold(imagem)
    imgAdaptThresh = adaptiveThreshold(imagem)
    displayImagem('regular threshold', imgRegularThresh, 'adaptive thresold', imgAdaptThresh)
    
main()