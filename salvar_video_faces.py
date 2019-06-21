# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 18:49:30 2019

@author: filipe.teixeira
"""

import cv2
import os
 
from os.path import isfile, join
 
def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
 
    #classificar nomes dos arquivos
    files.sort(key = lambda x: int(x[5:-4]))
 
    for i in range(len(files)):
        filename=pathIn + files[i]
        #ler cada arquivo
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        print(filename)
        #inserir os frames em uma matriz
        frame_array.append(img)
 
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
 
    for i in range(len(frame_array)):
        #gravando as imagens a partir do array
        out.write(frame_array[i])
    out.release()
 
def main():
    pathIn= './data/ImagesFaces/'
    pathOut = 'Avenger - Tony Stark.avi'
    fps = 25.0
    convert_frames_to_video(pathIn, pathOut, fps)
 
if __name__=="__main__":
    main()