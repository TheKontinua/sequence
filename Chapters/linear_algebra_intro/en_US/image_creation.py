# Import necessary modules
# numpy is the numerical python library
# PIL is python image library
import numpy as np
import PIL
from PIL import Image
from PIL import ImageOps

# Create a 10 by 10 pixel bitmap image. 
# Using a decimal point ensure python see the values as floating point numbers
# Some image operations assume floats
bitmapArray = np.array([
[0., 0., 0., 0., 1., 0., 0., 0., 1., 0.],
[0., 0., 0., 0., 1., 1., 1., 1., 1., 1.],
[0., 0., 0., 0., 1., 0., 0., 0., 1., 0.],
[0., 0., 0., 0., 1., 0., 0., 0., 1., 0.],
[0., 0., 0., 0., 1., 0., 0., 0., 1., 0.],
[0., 0., 0., 0., 1., 0., 0., 0., 1., 0.],
[0., 0., 0., 0., 1., 0., 0., 0., 1., 0.],
[0., 0., 0., 0., 1., 1., 1., 1., 1., 1.],
[0., 0., 0., 0., 1., 0., 0., 0., 1., 0.],
[0., 0., 0., 0., 1., 0., 0., 0., 1., 0.]])

# Image.fromarray assumes a range of 0 to 255, so scale by 255
myImage = Image.fromarray(bitmapArray*255)
myImage.show()
# A window opens with an image so tiny you might think nothing is there
# Zoom in to see the pattern  

# Transpose the array, create an image, and then show it. 
# Note that you operate on the original array (not the image)
# Remember to zoom in to see the pattern 
myImageTransposed = bitmapArray.transpose()
myImageTransposed.show()

# Invert the array. You'll use the NumPy invert method.
# The invert method assumes integer values. You need to convert the data type
# Numpy has a method for that
intBitmapArray = np.asarray(bitmapArray,dtype="int")
invertedArray = np.invert(intBitmapArray)

# Take a look at the array
invertedArray
# The values range from -2 to -1. Image values are positive.
# You need to change the range so the values are from 0 to 255
# Further you need to change back to floating point values because
# the PIL method requires them

invertedArray = (invertedArray + 2)*1.0
invertedImage = Image.fromarray(255*invertedArray)
invertedImage.show()
# Zoom in on the image and compare the pattern with the original

