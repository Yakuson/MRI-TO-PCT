#!/usr/bin/env python
import os
from pathlib import Path
import cv2
import numpy as np
import matplotlib.pyplot as plt
os.chdir(Path(__file__).parent.resolve())

def testInverse():
    image_path = askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image_normalized = image / 255.0
    c = 1.0  # Scaling constant
    inverse_log_scaled = c * np.log(1 + (1 / (image_normalized)))

    inverse_log_scaled = (255 * inverse_log_scaled / np.max(inverse_log_scaled)).astype(np.uint8)
    # Save the resulting image
    cv2.imwrite('inverse_log_scaled_image.png', inverse_log_scaled)
