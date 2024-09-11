import cv2
import os
import numpy as np

# Função para detectar carros
def detectar_carros(imagem):
    img = np.array(imagem)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sobel = cv2.Sobel(gray, -1, 1, 1)
    cv2.imshow("imagem", sobel)
    cv2.waitKey(0)

  #  thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 1)
    _, thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow("imagem", thresh)
    cv2.waitKey(0)

    contornos, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for contorno in contornos:
        # Filtrar pequenos objetos (ruído)
        if cv2.contourArea(contorno) > 500:
            # Desenhar caixa delimitadora ao redor do carro
            x, y, w, h = cv2.boundingRect(contorno)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("imagem", img)
    cv2.waitKey(0)
   # for (x,y,w,h) in thresh:
    #    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)






def main():

    os.chdir(r"D:\download v2\ras capacitação\Capacitacao\Missão 2\Atividade 2\\Imagens - Atividade 02\Tarefa-01")
    estradaVazia = cv2.imread("street-00.jpg")
    estradaComCarro = cv2.imread("street-01.jpg")

    deteccao = detectar_carros(estradaComCarro)

    # Mostrar a imagem com os carros detectados
    cv2.imshow('Detecção de Carros', deteccao)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()