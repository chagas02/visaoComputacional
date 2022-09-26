#Apresentando os primeiros comando do Opencv

import cv2
imagem = cv2.imread('rodovia.png')

print('Largura em pixels: ', end='')
print(imagem.shape[1])
print("Altura em pixels: ",  end='')
print(imagem.shape[0])
print('Qtde de canais: ', end='')
print(imagem.shape[2])
cv2.imshow("Nome da janela", imagem)
cv2.waitKey(0)
cv2.imwrite("saida.jpg", imagem)

#substituindo as imagens por uma cor
for y in range(0, imagem.shape[0]):
   for x in range(0, imagem.shape[1]):
     imagem[y, x] = (90,100, 125) #aqui você define a cor
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)

#observe que a diferença aqui fica por conta do parâmetro do salto
for y in range(0, imagem.shape[0], 10): #percorre linhas
   for x in range(0, imagem.shape[1], 10): #percorre colunas
     imagem[y:y+5, x: x+5] = (0,255,255)
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)