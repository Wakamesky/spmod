# -*- coding : utf-8 -*-

"""
y = -t^80 + t の多項式補間
シンプルな多項式補間で, ノルムは関係ない
"""

# import required packages

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

t_0 = np.array(np.linspace(start=0, stop=1.0, num=11, dtype=float))
t_1 = np.array(np.linspace(start=0, stop=1.0, num=1100, dtype=float))
print(t_0)
# t (1, 15)

y = -np.power(t_0, 80) + t_0
ground_truth = -np.power(t_1, 80) + t_1
Phi = np.vander(t_0)
x = np.dot(np.linalg.inv(Phi),  y.transpose())

# y (1, 15)
# Phi (15, 15)
print("y : ", y, " y_shape : ", np.shape(y))
print("Phi : ", Phi, " Phi_shape : ", np.shape(Phi))
print("x : ", x, " x_shape : ", np.shape(x))

# Get Polynominal interpolation
polynominal = np.poly1d([i for i in x])
print(polynominal)
p = [p for p in polynominal(t_1)]
# print(p)

# Plot data
plt.plot(t_0, y, "o", label="data")
plt.plot(t_1, ground_truth, "--", label="ground_truth")
plt.plot(t_1, p, "--", label="poly")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.show()