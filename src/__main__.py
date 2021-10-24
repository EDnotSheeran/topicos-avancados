import cv2

# Caminho da imagem
imgPath = r'Material/inputs/lena.jpg'
outputsPath = r'Material/outputs/'

# Faz a leitura da imagem e converte em uma matriz
imgUnchanged = cv2.imread(imgPath, cv2.IMREAD_UNCHANGED)
imgColor = cv2.imread(imgPath, cv2.IMREAD_COLOR)
imgGreyScale = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)

# Exibe a imagem
cv2.imshow('Original', imgUnchanged)
cv2.imshow('Colorida', imgColor)
cv2.imshow('Preto e Branco', imgGreyScale)

# Faz o programa para nessa linha te
cv2.waitKey()

# Salva a imagem
cv2.imwrite(outputsPath + 'color.jpg', imgColor)
cv2.imwrite(outputsPath + 'grayscale.jpg', imgGreyScale)

# Fecha as janelas
cv2.destroyAllWindows()
