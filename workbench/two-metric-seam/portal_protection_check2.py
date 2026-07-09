import sympy as sp
# symbolic proof of det(aI+bX) = sum_n a^{4-n} b^n e_n(X) for generic 4x4 X
a,b = sp.symbols('a b')
X = sp.Matrix(4,4, lambda i,j: sp.Symbol(f'x{i}{j}'))
lamda = sp.symbols('lam')
cp = X.charpoly(lamda).as_expr()  # lam^4 - e1 lam^3 + e2 lam^2 - e3 lam + e4
e = [1]
e.append( -cp.coeff(lamda,3))
e.append(  cp.coeff(lamda,2))
e.append( -cp.coeff(lamda,1))
e.append(  cp.coeff(lamda,0))
lhs = (a*sp.eye(4)+b*X).det()
rhs = sum(a**(4-n)*b**n*e[n] for n in range(5))
print("(a') det(aI+bX) == sum a^{4-n} b^n e_n(X):", sp.expand(lhs-rhs)==0)
