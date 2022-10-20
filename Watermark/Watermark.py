import cv2
import numpy as np
import glob
import os

logo = cv2.imread("mylogo.png")
h_logo, w_logo, _ = logo.shape
images_path = glob.glob("images/*.*")#Percorre tudo que está entro da pasta images
print("Adding watermark")# Print informativo


for img_path in images_path:
    img = cv2.imread(img_path)
    h_img, w_img, _ = img.shape
    # Pega o canto da imagem para colocar o logo (Possivel alterar posição)
    center_y = int(h_img / 1.01) #Coloque 2 para alterar para o centro
    center_x = int(w_img / 1.01)#Coloque 2 para alterar para o centro
    top_y = center_y - int(h_logo / 1)#Coloque 2 para alterar para o centro
    left_x = center_x - int(w_logo / 1)#Coloque 2 para alterar para o centro
    bottom_y = top_y + h_logo
    right_x = left_x + w_logo
    # Pega ROI
    roi = img[top_y: bottom_y, left_x: right_x]
    # Adiciona o logo ao Roi
    result = cv2.addWeighted(roi, 1, logo, 0.3, 0)
    # Troca o ROI na imagem
    img[top_y: bottom_y, left_x: right_x] = result
    filename = os.path.basename(img_path)
    cv2.imwrite("images/Copies/"+ filename , img)

