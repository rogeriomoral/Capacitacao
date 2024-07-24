import cv2
import os

# Função para carregar imagem do pc para o programa
def carregaImagemPC(filePath):
    imagem = cv2.imread(filePath)
    return imagem


def saveImage(imagem, diretorioDesejado):
    diretorio = diretorioDesejado
    #muda para o diretorio desejado
    os.chdir(diretorio)

    #salva
    cv2.imwrite('imagemSalva.jpg', imagem)


# Função para carregar imagem da Webcam
def carregaImagemWebcam():
    camera = cv2.VideoCapture(0) #abre a camera
    ret, frame = camera.read() #Lê apenas um frame
    camera.release() #Libera a webcam
    return frame

# Função para mostrar a imagem
def displayImagem(nomeJanela, imagem):
    cv2.imshow(nomeJanela, imagem) #Mostra a imagem
    cv2.waitKey(0) #Espera pressionar uma tecla

def main():

    imagemPC = carregaImagemPC(r"{caminhoImagemPC}")
    imagemWebcam = carregaImagemWebcam()
    
    displayImagem('Imagem Webcam', imagemWebcam)

    saveImage(imagemWebcam, r"Missão 2\Atividade 1\Programa 1\imagens")
    cv2.destroyAllWindows()

main()

    
    