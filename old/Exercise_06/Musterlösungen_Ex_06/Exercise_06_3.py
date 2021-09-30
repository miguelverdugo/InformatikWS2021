import numpy as np
import matplotlib.pyplot as plt


def find_star(image):
    pos = np.unravel_index(image.argmax(), image.shape)
    peak = np.max(image)
    return pos, peak

if __name__ == "__main__":
    img = np.genfromtxt("Photometry_example.txt")
    plt.imshow(img)
    plt.savefig("Plot.jpg")
    plt.show()
    print(find_star(img))
