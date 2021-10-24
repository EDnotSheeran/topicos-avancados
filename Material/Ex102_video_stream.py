# <!---------------------------------------------------------------------------->
# <!--                  IFSP - Instituto Federal de São Paulo                 -->
# <!--                       Tópicos Avançados (TPA A6)                       -->
# <!-- File       : Ex102_video_stream.py                                     -->
# <!-- Description: Script to convert the video stream in two different       -->
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
################################################################################
# Construct the argument parser and parse the arguments.
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", default=0, type=int,
                required=False, help="Video capture device ID or file path.")
args = vars(ap.parse_args())

# Hint: You can find more information about opening, converting and showing
#       images using OpenCV on official OpenCV docs (http://docs.opencv.org)

# TODO: Implement your solution here.
