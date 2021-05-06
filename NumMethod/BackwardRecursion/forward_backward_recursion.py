import numpy as np
from matplotlib import pylab


def iforward(w):
    if w == 0:
        return np.log(6) - np.log(5)
    return (1 / w) - (5 * iforward(w - 1))


def ibackward(f):
    if f >= 100:
        return 0
    return ((1 / (f + 1)) - ibackward(f + 1)) / 5


N = 34
iforward = [np.log(6) - np.log(5)]
for n in range(1, N + 1):
    iforward.append((1 / n) - (5 * iforward[n - 1]))

ibackward = [0] * (N + 1)
for n in range(N - 1, -1, -1):
    ibackward[n] = ((1 / (n + 1)) - ibackward[n + 1]) / 5

n = range(N + 1)
pylab.plot(n, iforward, label='Forward recursion')
pylab.plot(n, ibackward, label='Backward recursion')
pylab.ylim(-0.5, 2)
pylab.xlabel('$n$')
pylab.ylabel('$I(n)$')
pylab.legend()
pylab.show()
