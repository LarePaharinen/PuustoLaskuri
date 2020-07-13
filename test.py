from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
import functools as ft

i = Image.open("images/KuusiTukkiRajattu.png")
iar = np.array(i)

print(iar)