# -*- coding : utf-8 -*-

"""
Polynominal_interpolation_sin_wave
(Data with Gaussian noise)
正弦波(ガウシアンノイズ含む)の多項式補間
"""

# import required packages

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# prepare t-data
t_0 = np.array(np.linspace(start=0, stop=10, num=11))
t_1 = np.array(np.linspace(start=0, stop=10, num=11000))

# t_0, t_1  : (1, 15)
# print("t_0 : ", t_0, " t_0_shape : ", np.shape(t_0))
# print("t_1 : ", t_1, " t_1_shape : ", np.shape(t_1))

# prepare y-data
mu, sigma = 0.0, 0.2
y = np.sin(t_0) + np.random.normal(mu, sigma, 11)
ground_truth = np.sin(t_1)
Phi = np.vander(t_0)
x = np.dot(np.linalg.inv(Phi),  y.transpose())

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
print(polynominal(t_1))
print(p)

# Plot data
plt.plot(t_0, y, "o", label="data")
plt.plot(t_1, ground_truth, linestyle="--", color="orange", label="poly")
plt.plot(t_1, p, linestyle="-", color="red", label="poly")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.show()