import math
import sys
import sympy

symbols = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'asin': math.asin,
    'acos': math.acos,
    'atan': math.atan,
    'exp': math.exp,
    'log': math.log,
    'log10': math.log10,
    'sqrt': math.sqrt,
    'abs': math.fabs,
    'ceil': math.ceil,
    'floor': math.floor,
    'round': round,
    'pi': math.pi,
    'e': math.e,
}

def bisection_method(function, x_a, x_b, iterator):
    """
    x_a and x_b are intervals
    """
    i = 1
    x_r_before = 0
    list_sentence = []
    while True:
        f_a = eval(function, {**symbols, 'x': x_a})
        x_r = (x_a + x_b) / 2
        f_r = eval(function, {**symbols, 'x': x_r})
        sentence = f'i_{i}: x={x_r}'
        list_sentence.append(sentence)
        
        if i == iterator:
            print(list_sentence)
            break
        error = math.fabs((x_r - x_r_before) / x_r) * 100
        if error == 0:
            print(list_sentence)
            break

        sig = f_a * f_r
        if sig > 0:
            x_a = x_r
        elif sig < 0:
            x_b = x_r
        x_r_before = x_r
        i = i + 1


if __name__ == '__main__':
    # RESULT
    func_expresions = str(sys.argv[1])
    valor_a = float(sys.argv[2])
    valor_b = float(sys.argv[3])
    iterator = float(sys.argv[4])
    bisection_method(func_expresions, valor_a,valor_b, iterator)
