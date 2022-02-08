import pickle
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import cv2

from umbms import get_proj_path, verify_path, get_script_logger, null_logger

# Directory where the figures are stored as .png files
nt = os.path.join(get_proj_path(), 'output/A3F2_comp/nt')
t = os.path.join(get_proj_path(), 'output/A3F2_comp/t')

r5 = os.path.join(get_proj_path(), 'output/A3F2_comp/r5')
r10 = os.path.join(get_proj_path(), 'output/A3F2_comp/r10')
r15 = os.path.join(get_proj_path(), 'output/A3F2_comp/r15')

geom_params = [492, 493, 494, 495, 496, 497, 498, 499, 253, 256, 257, 251, 252, 255, 250, 254]
# pd.read_csv('metadata/umbmid_adi.csv')

# create figure
fig = plt.figure(figsize = (10,10))
plt.margins(x = 0.1, y = 0.1)
plt.axis('off')
# plt.title("Session 15")

# setting values to rows and column variables
rows = 4
columns = 4

im1 = []
im2 = []

# print(type(geom_params.keys()[0]))

for i in range (0,8):

    # geom_params.keys()[i]
    im1.append(img.imread(os.path.join(nt, ('das_%s.png' % geom_params[i]))))

    # Adds a subplot at the 1st position
    fig.add_subplot(rows, columns, i+1)

    # showing image
    plt.imshow(im1[i])
    plt.axis('off')
    plt.title("Scan %s" % geom_params[i])

for j in range (8,16):

    im1.append(img.imread(os.path.join(t, ('das_%s.png' % geom_params[j]))))

    # Adds a subplot at the 1st position
    fig.add_subplot(rows, columns, j+1)

    plt.imshow(im1[j])
    plt.axis('off')
    plt.title("Scan %s" % geom_params[j])

plt.show()
