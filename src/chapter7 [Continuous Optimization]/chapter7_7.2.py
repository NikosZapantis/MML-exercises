import sympy as sp

#! Theory using the equation at 7.15 page 238
#! Sources: [https://en.wikipedia.org/wiki/Loss_functions_for_classification  &  https://en.wikipedia.org/wiki/Stochastic_gradient_descent]

#? Variables
#? w1, w2: weights
#? x1, x2: input features
#? y: label (wiki report: ...follows from the fact that 1 and −1 are the only possible values for y)

w1, w2, x1, x2, y = sp.symbols('w1 w2 x1 x2 y', real=True)
w = sp.Matrix([w1, w2]) # weight vector
x = sp.Matrix([x1, x2]) # features vector

#? Logistic loss [l(w) = log(1 + exp(-y * (w.x)))]
loss = sp.log(1 + sp.exp(-y * (w.dot(x))))

#? Gradient of loss with respect to w (dl/dw)
grad = sp.Matrix([sp.diff(loss, wi) for wi in w])

#? SGD (stochastic update with batch size 1) [w := w - η * Q(w)] -> (Q(w) is the empirical risk)
h = sp.symbols('h', positive=True)
w_new = w - h * grad

#Display results
print("\n~ 7.2 Update equation with mini-batch size of one")
print("\nGradient of single-sample loss:")
sp.pprint(grad)

print("\nSGD update (mini-batch size = 1):")
sp.pprint(w_new)
