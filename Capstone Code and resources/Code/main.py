#!/usr/bin/env python
import os
from pathlib import Path
import cv2
import numpy as np
from tkinter.filedialog import askopenfilename
os.chdir(Path(__file__).parent.resolve())

image_path = askopenfilename()
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
image_float = np.float32(image)

log_image = np.log(image_float + 1) # Avoids log(0)
log_image = np.uint8(255 * log_image / np.max(log_image))

inverse_log_image = 255 - log_image  
cv2.imwrite('inverse_log_scaled_image.png', inverse_log_image)