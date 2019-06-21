# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 18:20:24 2019

@author: filipe.teixeira
"""

# Imoirtar bibliotecas
import cv2 
import os 
  
# Ler vídeo
cam = cv2.VideoCapture("C:\\Users\\filipe.teixeira\\Documents\\UNI-BH\\2019\\Computação Gráfica\\Detecção de Face\\avengers.mp4") 
  
try: 
    # criar diretório para armazenar os frames
    if not os.path.exists('data'): 
        os.makedirs('data') 
  
 
except OSError: 
    print ('Erro na criação do diretório') 
  
# frame 
currentframe = 0
  
while(True): 
      
    # ler frame 
    ret,frame = cam.read() 
  
    if ret: 
        # se ainda existirem frames
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name) 
  
        # grava frame como imagem
        cv2.imwrite(name, frame) 
  
        # incrementa contador de frame
        currentframe += 1
    else: 
        break
  
# libera espaço e janelas
cam.release() 
cv2.destroyAllWindows() 