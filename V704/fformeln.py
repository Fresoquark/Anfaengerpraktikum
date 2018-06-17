import sympy

def error(f, err_vars=None):
    from sympy import Symbol, latex
    s = 0
    latex_names = dict()

    if err_vars == None:
        err_vars = f.free_symbols

    for v in err_vars:
        err = Symbol('latex_std_' + v.name)
        s += f.diff(v)**2 * err**2
        latex_names[err] = '\\Delta_{' + latex(v) + '}'

    return latex(sympy.sqrt(s), symbol_names=latex_names)

#E, q, r = sympy.var('E_x q r')
r, a, b= sympy.var('R_m {1.92} {0.22}')
#f = E + q**2 * r
f = a * sympy.sqrt( r**2 + b * r)

print(f)
print(error(f))
print()
