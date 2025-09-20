import sympy as sp
from tabulate import tabulate

#! Sources: [https://docs.sympy.org/latest/modules/calculus/index.html] for (stationary points) Sympy version needed: [Version: 1.14.0]
#! [https://www.geeksforgeeks.org/python/python-sympy-subs-method-2/  &  https://docs.sympy.org/latest/modules/evalf.html]

def my_classify_stationary_points(f, symbol):
    f1 = sp.diff(f, symbol)
    f2 = sp.diff(f1, symbol)

    crit_pts = sp.solve(sp.Eq(f1, 0), symbol)
    
    res = []
    for cp in crit_pts:
        f_val = f.subs(symbol, cp)
        f2_val = f2.subs(symbol, cp)

        #? Classification for minimum, maximum or saddle
        if f2_val.is_real:
            if f2_val > 0:
                t = "minimum"
            elif f2_val < 0:
                t = "maximum"
            else:
                t = "saddle"
        else:
            t = "no-real"
        
        res.append({
            "x_exact": cp,
            "x_numeric": float(cp.evalf()),
            "f(x)": float(f_val.evalf()),
            "f''(x)": float(f2_val.evalf()),
            "type": t
        })
    
    return res


x = sp.symbols('x', real=True)
f = x**3 + 6*x**2  - 3*x - 5

res = my_classify_stationary_points(f, x)

# Display results
print(tabulate(res, headers="keys", floatfmt=".6f"))
