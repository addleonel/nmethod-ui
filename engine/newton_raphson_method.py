# I'm going to solve the root of a function using Newton-Raphson Method

# import modules
import math
import sys
import sympy


def runMethod(x_i):
    iterator = 0
    list_SENTENCE = []
    while True:
        f = function_ORIGINAL(x_i)
        f_d = function_DERIVED(x_i)
        x_next = x_i - (f / f_d)
        # print("valor de x:", iterator, ":", x_next)
        sentence = "valor de x en la iteracion"+str(iterator)+": "+str(x_next)
        list_SENTENCE.append(sentence)
        ERROR = math.fabs((x_next - x_i) / x_next) * 100
        if ERROR == 0:
            # print("la raiz cercano a ", x_i,"es: ", x_next)
            print(list_SENTENCE)
            break
        x_i = x_next
        iterator = iterator + 1



def function_ORIGINAL(x):
    f = 2 * math.sin(x) - x
    return f


def function_DERIVED(x):
    f_derived = 2 * math.cos(x) - 1
    return f_derived

termo = float(sys.argv[1])
runMethod(termo)
# RESULT

