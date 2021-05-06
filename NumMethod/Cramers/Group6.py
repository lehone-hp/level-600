import matplotlib
import matplotlib.pylab as plt
import numpy as np

y1 = []
y2 = []
y3 = []
b = []

# I3 - I1 -I2 = 0 ...........eq1
# 5I1 + 10I3 - 220 = 0.......eq2
# 10I3 + 20I2 -u = 0.........eq3

det = np.linalg.det([[-1, -1, 1], [5, 0, 10], [0, 20, 10]])

for u in range(200, 241):
    b.append(u)

for u in range(200, 241):
    det1 = np.linalg.det([[0, -1, 1], [220, 0, 10], [u, 20, 10]])
    i1 = det1 / det
    y1.append(i1)

for u in range(200, 241):
    det2 = np.linalg.det([[-1, 0, 1], [5, 220, 10], [0, u, 10]])
    i2 = det2 / det
    y2.append(i2)

for u in range(200, 241):
    det3 = np.linalg.det([[-1, -1, 0], [5, 0, 220], [0, 20, u]])
    i3 = det3 / det
    y3.append(i3)

plt.plot(b, y1, label="i 1")
plt.plot(b, y2, label="i 2")
plt.plot(b, y3, label="i 3")
plt.xlabel('U (voltage)')
plt.ylabel('I (Current)')
plt.legend()
plt.show()
