#Espelhando uma imagem
import cv2
img = cv2.imread('rodovia.png')
cv2.imshow("Original", img)

flip_horizontal = img[::-1,:]#comando equivalente: flip_horizontal = cv2.flip(img, 1)
cv2.imshow("Flip Horizontal", flip_horizontal)
cv2.imwrite("espelhada_h.jpg", flip_horizontal)

flip_vertical = img[:,::-1] #comando equivalente: flip_vertical = cv2.flip(img, 0)
cv2.imshow("Flip Vertical", flip_vertical)
cv2.imwrite("espelhada_v.jpg", flip_vertical)

flip_hv = img[::-1,::-1] #comando equivalente: flip_hv = cv2.flip(img, -1)
cv2.imshow("Flip Horizontal e Vertical", flip_hv)
cv2.imwrite("espelhada_hv.jpg", flip_hv)

cv2.waitKey(0)