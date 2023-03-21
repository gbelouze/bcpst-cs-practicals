import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rc('image', cmap='gray')
norm = mpl.colors.Normalize(vmin=0, vmax=255)

im = np.outer(np.arange(10), np.arange(10))
im[0, :] = 255
print(im)
plt.imshow(im, norm=norm)
plt.show()
