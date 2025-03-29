import warnings
import numpy as np
from sympy import symbols, sympify, lambdify

x = symbols('x')

def get_safe_function(expr_str):
    try:
        expr_str = expr_str.replace("np.", "")
        expr = sympify(expr_str)
        f_raw = lambdify(x, expr, 'numpy')
        
        def safe_f(x_val):
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", category=RuntimeWarning)
                return f_raw(x_val)
        
        return safe_f
    except Exception:
        return None
