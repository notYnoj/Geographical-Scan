import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from netCDF4 import Dataset
path = "/Users/jonathanalvarado/Desktop/Geography Scanner/data"
file = Dataset(path + '/data.nc', 'r')
elevation2 = file.variables['NASADEM_HGT'][:]
latitude = file.variables['lat'][:]
longitude = file.variables['lon'][:]
plt.figure(figsize=(10, 10))
elevation = np.flipud(elevation2)
plt.imshow(elevation, cmap='terrain', origin='lower', 
           extent=[longitude.min(), longitude.max(), latitude.min(), latitude.max()])
plt.show()
