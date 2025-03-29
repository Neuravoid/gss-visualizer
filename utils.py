from sympy import symbols, sympify, lambdify
import numpy as np

x = symbols('x')

def get_safe_function(expr_str):
    try:
        expr_str = expr_str.replace("np.", "")
        expr = sympify(expr_str)
        return lambdify(x, expr, 'numpy')
    except Exception:
        return None

