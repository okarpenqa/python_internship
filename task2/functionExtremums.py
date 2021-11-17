from sympy import Symbol, Interval, maximum, minimum

t = ['3.1 10.3 -2.8 10.3', '2.1 8.8 -11.4 -5.6', '1.6 0.2 -20.8 38.5']
for value in t:
    a, b, c, d = map(float, value.split())
    x = Symbol('x')
    interval = Interval(-4, 1)
    f = a * x ** 3 + b * x ** 2 + c * x + d
    res_min = minimum(f, x, interval)
    res_max = maximum(f, x, interval)
    print(format(res_min, ' .4f'))
    print(format(res_max, ' .4f'))
    print('=========================')


