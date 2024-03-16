#Importing path and skimage i/o library 
import os.path
from skimage.io import imread
from skimage import data_dir
#reading the astronaut image
img = imread(os.path.join(data_dir, 'astronaut.png'))
#Slicing out the rocket 
img_slice = img.copy()
img_slice = img_slice[0:300,360:480]
plt.figure()
plt.imshow(img_slice)

