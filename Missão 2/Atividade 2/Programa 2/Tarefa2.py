import cv2
import os
import numpy as np


def detectar_invasores(imagem):
    #imagem cinza
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    #aplicando thresh
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    
    #aplicando morphology pra limpar a imagem
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10,10))
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    #pegando contornos
    contornos, _ = cv2.findContours(morph, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    #iterando para desenhar ao redor do invasor detectado
    for contorno in contornos:
        # Filtrar pequenos objetos 
        if cv2.contourArea(contorno) > 1500:
            # Desenhar caixa delimitadora ao redor
            x, y, w, h = cv2.boundingRect(contorno)
            cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return imagem

def main():

    os.chdir(r"D:\download v2\ras capacitação\Capacitacao\Missão 2\Atividade 2\Imagens - Atividade 02\Tarefa-02")
    invasor = cv2.imread("larapio.jpg")
    porta = cv2.imread("porta1.jpg")
    cachorro = cv2.imread("kirra1.jpg")

    deteccao = detectar_invasores(invasor)
    # Mostrar a imagem com os carros detectados
    cv2.imshow('Detectar invasor', deteccao)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()