import numpy as np
import threading
from numpy.polynomial import polynomial

coefficients = [float(s) for s in input('Sequence of coefficients separated with spaces: ').split(' ')]
interval = [float(s) for s in input('Specify the interval: ').split(' ')]
a, b = interval[0], interval[1]
f = lambda x: polynomial.polyval(x, coefficients)
epsilon = .000001
results = []

def bisection(a, b):
    if a > b:
        return 'Improper interval'
    elif np.sign(f(a)) + np.sign(f(b)) == 0:
        c = (a + b)/2
        results.append(c)

        if abs(f(c)) < epsilon:
            return f"The root is {c}"

        d = a if np.sign(f(a)) == -np.sign(f(c)) else b

        bisection(min(c, d), max(c, d))
    else:
        return 'Cannot approximate, maybe adjust the interval?'

bisection(a, b)
print('')
print('Next steps of approximation')
for r in results:
    print(r)
