# I'm going to solve a function using bisection method
import math
import sys
import numpy as np
from matplotlib import pyplot as plt


# x_a and x_b are intervals
def bisection_method(x_a, x_b):
    i = 0
    x_r_before = 0
    list_SENTENCE = []
    while True:
        f_a = function(x_a)
        x_r = (x_a + x_b) / 2
        f_r = function(x_r)
        sentence = "valor de x en la iteracion", i, ":", x_r
        list_SENTENCE.append(sentence)
        if i > 0:
            ERROR = math.fabs((x_r - x_r_before) / x_r) * 100
            if ERROR == 0:
                print(list_SENTENCE)
                break

        sig = f_a * f_r
        if sig > 0:
            x_a = x_r
        elif sig < 0:
            x_b = x_r
        x_r_before = x_r
        i = i + 1


def function(x):
    f = math.sin(x)
    # print(f)
    return f


# graficar la funcion
def graphicoffunction():
    x = np.array(range(100))
    y = np.zeros(len(x))
    for i in range(-100, len(x)):
        y[i] = function(x[i])

    plt.plot(x, y)
    plt.show()


# RESULT
# valor_a = float(sys.argv[1])
# valor_b = float(sys.argv[2])

# bisection_method(valor_a,valor_b)
# bisection_method(0 , 1.4)
graphicoffunction()
