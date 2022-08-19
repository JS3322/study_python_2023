#유사도
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pandas as pd

def rgb_plot(fname):
    print('start check')

    img = Image.open(fname)
    img = img.convert('RGB')
    pixel_data = img.getdata()
    pixels = np.array(pixel_data)
    print(pixels.size)
    n = pixels.size
    xmin, xmax, ymin, ymax, zmin, zmax = 0, 255, 0, 255, 0, 255
    cmin, cmax = 0, 2
    xs = pixels[:, 0]
    ys = pixels[:, 1]
    zs = pixels[:, 2]
    color = np.array([(cmax - cmin) * np.random.random_sample() - cmin for i in range(n)])

    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection= '3d')
    ax.scatter(xs, ys, zs, c=color, marker='0', s=15, xmap="Greens")
    ax.set_xlabel('red', fontsize=14)
    ax.set_zlabel('green', fontsize=14)
    ax.set_Ylabel('blue', fontsize=14)

    plt.show()

    df = pd.DataFrame(pixels)






