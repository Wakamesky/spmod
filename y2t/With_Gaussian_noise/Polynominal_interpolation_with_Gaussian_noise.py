# -*- coding : utf-8 -*-

"""
y = 2 * t (ガウシアンノイズ含む) の多項式補間
リッジ回帰を利用
"""

# import required packages

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# prepare t-data
t_0 = np.array(np.linspace(start=1, stop=15, num=15))
t_1 = np.array(np.linspace(start=1, stop=15, num=15000))

# t_0, t_1  : (1, 15)
# print("t_0 : ", t_0, " t_0_shape : ", np.shape(t_0))
# print("t_1 : ", t_1, " t_1_shape : ", np.shape(t_1))

# prepare y-data
mu, sigma = 0.0, 0.5
y = 2 * t_0 + np.random.normal(mu, sigma, 15)

Phi15 = np.vander(t_0)

Phi = Phi15[:, 13:]

print(np.shape(Phi))
print(np.shape(y.transpose()))
x = np.dot(np.dot(np.linalg.inv(np.dot(Phi.transpose(), Phi)), Phi.transpose()), y.transpose())


# y (1, 15)
# Phi (15, 15)
# print("y : ", y, " y_shape : ", np.shape(y))
# print("Phi : ", Phi, " Phi_shape : ", np.shape(Phi))
# print("x : ", x, " x_shape : ", np.shape(x))

# Get Polynominal interpolation
print(x)
polynominal = np.poly1d([i for i in x])
print(polynominal)
p = polynominal(t_1)
# print(polynominal(t_1))
# print(p)

# Plot data
plt.plot(t_0, y, "o", label="data")
plt.plot(t_1, p, "-", color="red", label="poly")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.show()