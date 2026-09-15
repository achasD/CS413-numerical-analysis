import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd
from numpy import sin, cos, log, e
from typing import Callable

true = True

def get_number_of_iterations(
    a : float,
    b : float,
    tolerance : float
):
    return (b - a) / (2 ** ())

def bisection_by_iteration(
        f : Callable,
        a : float,
        b : float,
        iterations : int
):
    if f(a) * f(b) >= 0: raise ValueError("f(a) and f(b) must have opposite signs")
    c = (a + b) / 2
    for k in range(a, b + 1):
        if f(a) * f(c) < 0: b = c
        else: a = c
        print(f"{k} : c = {c}, f(c) = {f(c):.5}")
        c = (a + b) / 2

def bisection_with_error_tolerance(
        f : Callable,
        a : float,
        b : float,
        error_tolerance : float
) -> tuple[float, float, list]:
    if f(a) * f(b) >= 0: raise ValueError("f(a) and f(b) must have opposite signs")

    c = (a + b) / 2
    k = 0
    iterations = [(k, a, c, b)]

    while (b - a) / 2 > error_tolerance:
        if f(a) * f(c) < 0: b = c
        else: a = c

        c = (a + b) / 2
        k += 1
        iterations.append([k, a, c, b])
    return (c, (b - a) / 2, iterations)

def find_root_intervals(
    f : Callable,
    a : int,
    b : int,
    step : float = 1.0
) -> list[tuple[float, float]]:
    intervals = []
    while a < b:
        if f(a) * f(a + step) < 0: intervals.append((a, a + step))
        a += step
    return intervals

def f1_a(x): return (x ** 3) - 9  # x^3 = 9
def f1_b(x): return (3 * (x ** 3)) + (x ** 2) - x - 5 # 3x^3 + x^2 = x + 5
def f1_c(x): return ((cos(x)) ** 2) - x + 6 # cos^2(x) + 6 = x

def f2_a(x): return (x ** 5) + x - 1 # x^5 + x = 1
def f2_b(x): return sin(x) - (6 * x) - 5 # sin(x) = 6x + 5
def f2_c(x): return log(x) + (x ** 2) - 3 # ln(x) + x^2 = 3

def f3_a(x): return (2 * (x ** 3)) - (6 * x) - 1 # 2x^3 -  6x - 1
def f3_b(x): return (e ** (x - 2)) + (x ** 3) - x # e^(x-2) + x^3 - x
def f3_c(x): return 1 + (5 * x) - (6 * (x ** 3)) - (e ** (2 * x)) # 1 + 5x - 6x^3 - e^(2x)

def from_dict(d : dict):
    for k in d.keys():
        c = bisection_with_error_tolerance(d[k][0], d[k][1], d[k][2], d[k][3])
        print(f"{k}\n", pd.DataFrame(c[2], columns=['k', 'a_k', 'c_k', 'b_k']), "\n")

def find_root_intervals_from_dict(
    d : dict,
    step : int = 1.0,
    a : float = -10,
    b : float = 10
) -> dict[str, list[tuple[float, float]]]:
    d_intervals = {}
    for k in d.keys():
        d_intervals[k] = find_root_intervals(d[k][0], a, b, step)

    return d_intervals

def bisection_by_dict(d : dict) -> dict[str, dict[tuple[float, float], tuple[float, float, list]]]:
    intervals = find_root_intervals_from_dict(d, 0.75)
    results = {}
    
    for k in intervals.keys():
        k_intercepts = {}
        for i in intervals[k]:
            k_intercepts[i] = (bisection_with_error_tolerance(
                d[k][0],
                i[0],
                i[1],
                d[k][3]
            ))
        results[k] = k_intercepts
    
    return results



f_list = {
    #name : (function, lower terminal, upper terminal, error_tolerance)
    "f1_a" : (f1_a, 2, 3, 1e-6),
    "f1_b" : (f1_b, 1, 2, 1e-6),
    "f1_c" : (f1_c, 6, 7, 1e-6),
    "f2_a" : (f2_a, 0, 1, 1e-8),
    "f2_b" : (f2_b, -1, 0, 1e-8),
    "f2_c" : (f2_c, 1, 2, 1e-8),
    "f3_a" : (f3_a, -1, 0, 1e-6),
    "f3_b" : (f3_b, 0.5, 1, 1e-6),
    "f3_c" : (f3_c, 0.5, 1, 1e-6),
}

results = bisection_by_dict(f_list)
for k in results.keys():
    r_k = results[k]

    for i in r_k.keys():
        print(f"Intercept in interval {i} for function {k}:")
        print(pd.DataFrame(r_k[i][2], columns=['k', 'a_k', 'c_k', 'b_k']))
        print()

# Plot f3
x = np.linspace(-2, 2)
plt.figure(figsize=(5,5))
plt.grid(true)
plt.plot(x, f3_a(x), "r")
for i in results["f3_a"].keys():
    r = results["f3_a"][i][0]
    plt.plot(r, f3_a(r), "y*")

plt.figure(figsize=(5,5))
plt.grid(true)
plt.plot(x, f3_b(x), "b")
for i in results["f3_b"].keys():
    r = results["f3_b"][i][0]
    plt.plot(r, f3_b(r), "y*")

plt.figure(figsize=(5,5))
plt.grid(true)
plt.plot(x, f3_c(x), "g")
for i in results["f3_c"].keys():
    r = results["f3_c"][i][0]
    plt.plot(r, f3_c(r), "y*")

plt.show()