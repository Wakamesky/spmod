# -*- coding : utf-8 -*-

"""
スパースモデリング
"""

# import required packages

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cvxpy as cp

t_0 = np.array(np.linspace(start=0, stop=1.0, num=11, dtype=float))
t_1 = np.array(np.linspace(start=0, stop=1.0, num=1100, dtype=float))
# print(t_0)
# t (1, 15)

y = -np.power(t_0, 80) + t_0
ground_truth = -np.power(t_1, 80) + t_1

# Vandermondeの最右列を書かないと初期化してないとうるさい
# Without this initializeing, scolded by numpy in following part, making vandermonde matrix.
Phi = np.array([[1.0] for i in range(0, 11)])
print(Phi)
print(np.shape(Phi))

for m in range(1, 81):
    temp = np.power(t_0.transpose(), m)
    temp = np.c_[temp]
    Phi = np.concatenate([temp, Phi], axis=1)
    # print(np.shape(Phi))

print(Phi)

x = cp.Variable(81)
objective = cp.Minimize(cp.norm(x, 1))
constraints = [Phi * x == y.transpose()]
prob = cp.Problem(objective=objective, constraints=constraints)

result = prob.solve()

print(x.value)

"""
# y (1, 15)
# Phi (15, 15)
print("y : ", y, " y_shape : ", np.shape(y))
print("Phi : ", Phi, " Phi_shape : ", np.shape(Phi))
print("x : ", x, " x_shape : ", np.shape(x))
"""
# Get Polynominal interpolation
polynominal = np.poly1d([i for i in x.value])
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
