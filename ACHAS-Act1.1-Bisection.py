import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd
from numpy import sin, cos, log, e
from typing import Callable

def get_number_of_iterations(
    a : float,
    b : float,
    tolerance : float
):
    return (b - a) / (2 ** ())

def bisection(
        
):
    pass

def bisection_with_error_tolerance(
        f : Callable,
        a : float,
        b : float,
        error_tolerance : float
):
    if f(a) * f(b) >= 0: raise ValueError("f(a) and f(b) must have opposite signs")

    c = (a + b) / 2
    k = 0
    iterations = [[k, a, c, b]]

    while (b - a) / 2 > error_tolerance:
        if f(a) * f(c) < 0: b = c
        else: a = c

        c = (a + b) / 2
        k += 1
        iterations.append([k, a, c, b])
    return (c, (b - a) / 2, iterations)

def f1_a(x): return (x ** 3) - 9  #x^3 = 9
def f1_b(x): return (3 * (x ** 3)) + (x ** 2) - x - 5 #3x^3 + x^2 = x + 5
def f1_c(x): return ((cos(x)) ** 2) - x + 6 #cos^2(x) + 6 = x

def f2_a(x): return (x ** 5) + x - 1 #x^5 + x = 1
def f2_b(x): return sin(x) - (6 * x) - 5 #sin(x) = 6x + 5
def f2_c(x): return log(x) + (x ** 2) - 3 #ln(x) + x^2 = 3

def f3_a(x): return (2 * (x ** 3)) - (6 * x) - 1
def f3_b(x): return (e ** (x - 2)) + (x ** 3) - x
def f3_c(x): return 1 + (5 * x) - (6 * (x ** 3)) - (e ** (2 * x))

a = 0
b = 10

f1_tolerance = 1e-6

c1_a = bisection_with_error_tolerance(f1_a, 2, 3, f1_tolerance)
c1_b = bisection_with_error_tolerance(f1_b, 1, 2, f1_tolerance)
c1_c = bisection_with_error_tolerance(f1_c, 6, 7, f1_tolerance)

df1_a = pd.DataFrame(c1_a[2], columns=['k', 'a_k', 'c_k', 'b_k'])
df1_b = pd.DataFrame(c1_b[2], columns=['k', 'a_k', 'c_k', 'b_k'])
df1_c = pd.DataFrame(c1_c[2], columns=['k', 'a_k', 'c_k', 'b_k'])

print(df1_a)
print(df1_b)
print(df1_c)

f2_tolerance = 1e-8
c2_a = bisection_with_error_tolerance(f2_a, 0, 1, f2_tolerance)
c2_b = bisection_with_error_tolerance(f2_b, -1, 0, f2_tolerance)
c2_c = bisection_with_error_tolerance(f2_c, 1, 2, f2_tolerance)

df2_a = pd.DataFrame(c2_a[2], columns=['k', 'a_k', 'c_k', 'b_k'])
df2_b = pd.DataFrame(c2_b[2], columns=['k', 'a_k', 'c_k', 'b_k'])
df2_c = pd.DataFrame(c2_c[2], columns=['k', 'a_k', 'c_k', 'b_k'])

print(df2_a)
print(df2_b)
print(df2_c)

c3_a = bisection_with_error_tolerance(f3_a, -1, 0, f1_tolerance)
c3_b = bisection_with_error_tolerance(f3_b, 0.5, 1, f1_tolerance)
c3_c = bisection_with_error_tolerance(f3_c, 0.5, 1, f1_tolerance)

df3_a = pd.DataFrame(c3_a[2], columns=['k', 'a_k', 'c_k', 'b_k'])
df3_b = pd.DataFrame(c3_b[2], columns=['k', 'a_k', 'c_k', 'b_k'])
df3_c = pd.DataFrame(c3_c[2], columns=['k', 'a_k', 'c_k', 'b_k'])

print(df3_a)
print(df3_b)
print(df3_c)