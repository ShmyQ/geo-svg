import matplotlib.pyplot as plt
import numpy as np

phi = np.radians(360 / np.power((1 + np.sqrt(5)) / 2, 2))

n = np.arange(0, 2000, 55)
theta = phi * n
r = 2 * n
x = np.multiply(r, np.cos(theta))
y = np.multiply(r, np.sin(theta))

for rotate in np.arange(0, 360, 30):
    s = np.sin(np.radians(rotate))
    c = np.cos(np.radians(rotate))
    x1 = np.subtract(np.multiply(x, c), np.multiply(y, s))
    y1 = np.add(np.multiply(x, s), np.multiply(y, c))
    plt.plot(x1, y1, "k-")
    plt.plot(x1 * -1, y1, "k-")

plt.gcf().set_size_inches(10, 10)
plt.axis("off")
plt.gca().set_position([0, 0, 1, 1])
plt.savefig("test.svg")
