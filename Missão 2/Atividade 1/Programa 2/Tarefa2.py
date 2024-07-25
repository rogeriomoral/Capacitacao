import cv2
import os

#Função para mostrar as dimensões de uma imagem
def mostrarDimensoes(imagem):
    canais = ''

    # Obter as dimensões da imagem
    if len(imagem.shape) > 2:
        altura, largura, canais = imagem.shape
    #caso na imagem cinza
    else:
        altura, largura = imagem.shape

    # Exibir as dimensões
    print(f"Altura: {altura} pixels")
    print(f"Largura: {largura} pixels")
    print(f"Canais: {canais}")

#Função para converter a imagem para cinza
def converterGrayscale(imagem):
    return cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

#Função para converter a imagem para HSV
def converterHSV(imagem):
    return cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)


def main():
    #vai pro diretorio da imagem
    os.chdir(r"D:\download v2\ras capacitação\Capacitacao\Missão 2\Atividade 1\imagens")

    imagem = cv2.imread("imagemSalva.jpg")
    mostrarDimensoes(imagem)

    imagem_cinza = converterGrayscale(imagem)
    print("=" * 20)
    print("Dimensões em grayscale:")
    mostrarDimensoes(imagem_cinza)

    imagemHSV = converterHSV(imagem)
    cv2.imshow("Imagem HSV", imagemHSV)
    cv2.waitKey(0)

main()