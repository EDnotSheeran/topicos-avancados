# <!---------------------------------------------------------------------------->
# <!--                  IFSP - Instituto Federal de São Paulo                 -->
# <!--                       Tópicos Avançados (TPA A6)                       -->
# <!-- File       : Ex101_color_spaces.py                                     -->
# <!-- Description: Script to convert the input images in two different       -->
# <!--            : color spaces (RGB and HSV)                                -->
# <!-- Author     : Fabricio Batista Narcizo (narcizo[at]itu[dot]dk)          -->
# <!-- Information: No additional information                                 -->
# <!-- Date       : 10/10/2021                                                -->
# <!-- Change     : 10/10/2021 - Creation of this script                      -->
# <!-- Review     : 10/10/2021 - Finalized                                    -->
# <!---------------------------------------------------------------------------->

__version__ = "$Revision: 2021101001 $"

################################################################################
import numpy as np
import argparse
import cv2

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import os

imagePath = f"{os.path.dirname(os.path.abspath(__file__))}/inputs/lena.jpg"

################################################################################
# Construct the argument parser and parse the arguments.
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default=(imagePath), type=str,
                required=False, help="Path to the image.")
args = vars(ap.parse_args())

# Create the Matplotlib window.
fig = plt.figure()
# Hint: You can find more information about opening, converting and showing
#       images using OpenCV on official OpenCV docs (http://docs.opencv.org)

# TODO: Implement your solution here.

print(fig)

# Show the final image.
plt.show()
