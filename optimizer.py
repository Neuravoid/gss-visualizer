import math
from scipy.misc import derivative

def find_the_trend(f, a_current, b_current, x1, x2, extreme_type="max"):
    """
    Determines the new interval based on derivatives at x1 and x2.
    a_current and b_current are the current interval boundaries.
    """
    der1 = derivative(f, x1, dx=1e-3)
    der2 = derivative(f, x2, dx=1e-3)
    if extreme_type == "max":
        if der1 > der2:
            return (x1, b_current)
        else:
            return (a_current, x2)
    else:
        if der1 < der2:
            return (x1, b_current)
        else:
            return (a_current, x2)


def gold_ratio_search(f, a, b, extreme_type="max", tol=1e-4, show=False):
    ratio = (math.sqrt(5) - 1) / 2  # ~0.618
    step = 0
    history = []
    const_a, const_b = a, b  # Original interval for plotting

    while abs(b - a) > tol:
        step += 1
        x1 = b - ratio * (b - a)
        x2 = a + ratio * (b - a)
        f1, f2 = f(x1), f(x2)
        history.append((a, b, x1, x2, f1, f2))

        if f1 == f2:
            a, b = find_the_trend(f, a, b, x1, x2, extreme_type)
        elif (f1 > f2 and extreme_type == "max") or (f1 < f2 and extreme_type == "min"):
            b = x2
        else:
            a = x1

        if show:
            print(f"Step {step}: range = [{a:.5f}, {b:.5f}]")

    opt_x = (a + b) / 2
    if show:
        print(f"*** Final range: [{a:.5f}, {b:.5f}] => Optimum x = {opt_x:.5f}")
    return opt_x, history, const_a, const_b