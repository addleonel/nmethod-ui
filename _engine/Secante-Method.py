# I'm going to solve a function using secant method
import math
import sys

def secant_METHOD(x_i, x_i_1):
    iterator = 0
    list_SENTENCE=[]
    while True:
        f_i = function(x_i)
        f_i_1 = function(x_i_1)
        Rest = x_i - x_i_1
        x_next = x_i - ((f_i * Rest) / (f_i - f_i_1))
        sentence = "valor de x en la iteracion", iterator, ":", x_next
        list_SENTENCE.append(sentence)
        ERROR = math.fabs((x_next - x_i) / x_next)*100
        if ERROR == 0:
            # print("the answer: ", x_next)
            print(list_SENTENCE)
            break
        x_i_1 = x_i
        x_i = x_next
        iterator = iterator + 1


def function(x):
    f = math.exp(-x) - x
    return f


# RESULT
valor_a = float(sys.argv[1])
valor_b = float(sys.argv[2])
secant_METHOD(valor_a, valor_b)
# secant_METHOD(2, 5)
