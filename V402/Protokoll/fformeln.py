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
a0, a2, la ,b = sympy.var('A_0 A_2 \lambda b')
#f = E + q**2 * r
f = b * a2/(la**3 * sympy.sqrt(a0+a2/la**2))

print(f)
print(error(f))
print()
