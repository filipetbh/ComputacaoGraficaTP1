# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 18:55:30 2019

@author: filipe.teixeira
"""

import cv2
import face_recognition
import glob, os
#from matplotlib import pyplot as plt
#plt.rcParams['figure.figsize'] = (224, 224)


def faceDetecter(path, facefilename, imagem, id_frame):
    try: 
                         
        face_encod = face_recognition.face_encodings(imagem)[0]

        faces_conhecidas = [
            face_encod
        ]
        
        imagem2 = cv2.imread(path)
  
        face_locations = []

        rgb_frame = imagem2[:, :, ::-1]

        #Detecta todas as faces em uma imagem
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        

        face_names = []
        match = False
        for face_encoding in face_encodings:
            # Compara a imagem de busca com todos os rostos existentes na imagem atual.
            match = face_recognition.compare_faces(faces_conhecidas, face_encoding, tolerance=0.6)
        
            name = None
            if match[0]:
                name = "Tony Stark"
                print(name, 'encontrado no frame:', id_frame)

            face_names.append(name)

        #Aplica a label nas faces encontradas
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            if not name:
                continue

            #Desenha um retangulo  em torno da face
            cv2.rectangle(imagem2, (left, top), (right, bottom), (0, 127, 255), 2)

            #Inclui o nome da face identificada
            cv2.rectangle(imagem2, (left, bottom - 25), (right, bottom), (0, 127, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(imagem2, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        cv2.imwrite(facefilename, imagem2)
        print ('Salvando a imagem:', facefilename)
        

    except:
        print ('Erro ao converter a imagem')
   
        

# Modulo principal
if __name__ == "__main__":
    img = cv2.imread('imagem/tonyStark.jpg')

    # Armazena o caminho informado na variavel d
    d = input ('Informe o diretorio de imagens:')
     
    if not os.path.exists(d):
        raise Exception('O diretorio informado nao existe')
         
    # 'Navega' ao diretorio informado
    os.chdir(d)
    # os.path.abspath(os.curdir) tambem retorna o diretorio corrente
    print ('Diretorio corrente:', os.getcwd())
 
    # Cria o diretorio para armazenar as imagens P&B
    os.mkdir('ImagesFaces')
     
    # Convertendo todas as imagens JPEG para escalas de cinza
    for fn in glob.glob('*.jpg'):
            print ('Processando:', fn)
 
            # obtem o nome do arquivo sem a extensao
            f = glob.os.path.splitext(fn)[0]
 
            # Converte a imagem escala de cinza e salva no diretorio GrayImages
            faceDetecter(fn, 'ImagesFaces/' + f + '.jpg', img, f)
            
 
    print ('Concluido')