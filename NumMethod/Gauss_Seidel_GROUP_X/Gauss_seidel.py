from sympy import *
import matplotlib.pylab as plt
import numpy as np

ITERATION_LIMIT = 20

i1, i2, i3 = symbols("i1, i2, i3")
A = Matrix([[4, -1, -3], [0, -1, 3], [-2, 0, 3]])
b = Matrix([-4, 44, 24])
sol = linsolve((A, b), [i1, i2, i3])

# exact solution
print("Solution from linsolve: " + str(sol))
I_exact = Array(sol.subs({i3: 44 / 9}), 3)

A = np.array(A).astype(np.float64)
b = np.array(b).astype(np.float64)
print(A)
print(b)
print(I_exact)
I_ini = np.zeros_like(b)
I2 = np.zeros(ITERATION_LIMIT)
for i in range(0, ITERATION_LIMIT):
    I_new = np.zeros_like(I_ini)
    print("Iteration {0}: {1} \n\n".format(i, I_ini))
    for j in range(A.shape[0]):
        print("for i =", j)
        print(A[j, :j])
        print(I_new[:j])
        s1 = np.dot(A[j, :j], I_new[:j])
        s2 = np.dot(A[j, j + 1:], I_ini[j + 1:])
        I_new[j] = (b[j] - s1 - s2) / A[j, j]
    I2[i] = I_new[1]
    I_ini = I_new

print("Solution N = {1}: {0}".format(I_ini, ITERATION_LIMIT))

rel_error_i2 = lambda x: np.absolute((x - I_exact[1]) / I_exact[1])

X = np.arange(ITERATION_LIMIT)
re_i2 = rel_error_i2(I2)

plt.plot(X, re_i2, label="re")
plt.xlabel('N (Iteration)')
plt.ylabel('RE_I2 (Relative error I2)')
plt.legend()
plt.show()
