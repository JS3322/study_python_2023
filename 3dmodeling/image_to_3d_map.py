# pip install opencv-python numpy matplotlib rasterio

import cv2
import numpy as np
import matplotlib.pyplot as plt
import rasterio

def load_elevation_data(file_path):
    with rasterio.open(file_path) as src:
        elevation_data = src.read(1)
    return elevation_data

def normalize_elevation_data(elevation_data):
    min_value = np.min(elevation_data)
    max_value = np.max(elevation_data)
    return (elevation_data - min_value) / (max_value - min_value)

def create_3d_map(elevation_data):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    x = np.arange(0, elevation_data.shape[1], 1)
    y = np.arange(0, elevation_data.shape[0], 1)
    x, y = np.meshgrid(x, y)
    ax.plot_surface(x, y, elevation_data, cmap='terrain', linewidth=0, antialiased=False)
    plt.show()

if __name__ == '__main__':
    file_path = 'path/to/your/dem_file.tif'
    elevation_data = load_elevation_data(file_path)
    normalized_data = normalize_elevation_data(elevation_data)
    create_3d_map(normalized_data)
