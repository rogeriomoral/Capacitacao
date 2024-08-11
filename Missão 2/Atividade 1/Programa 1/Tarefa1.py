import cv2
import os

# Função para carregar imagem do pc para o programa
def carregaImagemPC(filePath):
    return cv2.imread(filePath)

# Função para carregar imagem da Webcam
def carregaImagemWebcam():
    camera = cv2.VideoCapture(0) #abre a camera
    ret, frame = camera.read() #Lê apenas um frame
    camera.release() #Libera a webcam
    return frame

def saveImage(imagem, diretorioDesejado):
    diretorio = diretorioDesejado
    #muda para o diretorio desejado
    os.chdir(diretorio)

    #salva
    cv2.imwrite('imagemSalva.jpg', imagem)

# Função para mostrar a imagem
def displayImagem(nomeJanela, imagem):
    cv2.imshow(nomeJanela, imagem) #Mostra a imagem
    cv2.waitKey(0) #Espera pressionar uma tecla

def main():
    #vai pro diretorio da imagem
    os.chdir(r"D:\download v2\ras capacitação\Capacitacao\Missão 2\Atividade 1\imagens")

    imagemPC = carregaImagemPC("imagemSalva.jpg")
    imagemWebcam = carregaImagemWebcam()
    
    displayImagem('Imagem Webcam', imagemWebcam)

    saveImage(imagemWebcam, r"Missão 2\Atividade 1\imagens")
    cv2.destroyAllWindows()

main()

    
    