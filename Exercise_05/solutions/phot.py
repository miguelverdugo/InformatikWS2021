import numpy as np
import matplotlib.pyplot as plt


arr = np.genfromtxt("../Photometry_example.txt")

#plt.imshow(arr)
#plt.show()

maxi = np.max(arr)

print(maxi)

x, y = np.where(arr == maxi)

print(x[0], y[0])


