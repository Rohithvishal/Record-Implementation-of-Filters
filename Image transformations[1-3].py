i)Image Translation
import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("download(1).jpeg")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  
plt.title("Original Image")  
plt.axis('off')
#image translation
tx, ty = 100, 50  
M_translation = np.float32([[1, 0, tx], [0, 1, ty]])  
translated_image = cv2.warpAffine(image, M_translation, (image.shape[1], image.shape[0]))  
plt.imshow(cv2.cvtColor(translated_image, cv2.COLOR_BGR2RGB))  
plt.title("Translated Image")  
plt.axis('off')

ii) Image Scaling

#scaled image
fx, fy = 5.0, 2.0 
scaled_image = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
plt.imshow(cv2.cvtColor(scaled_image, cv2.COLOR_BGR2RGB))  
plt.title("Scaled Image")  
plt.axis('off')

iii)Image shearing

#image shearing
shear_matrix = np.float32([[1, 0.5, 0], [0.5, 1, 0]])  
sheared_image = cv2.warpAffine(image, shear_matrix, (image.shape[1], image.shape[0]))
plt.imshow(cv2.cvtColor(sheared_image, cv2.COLOR_BGR2RGB)) 
plt.title("Sheared Image") 
plt.axis('off')