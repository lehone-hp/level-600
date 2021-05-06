# Name: LENYA HOPE NEMBI
# Matricule: FE15P030
# Department: Software
# Course: Numerical Method CA


# Defining Function
def f(x, v):
    return (x ** 3) + (70.3 * x ** 2) + (1647.39 * x) - (v / 0.0268)


# Defining derivative of function
def g(x, v):
    return (3 * x ** 2) + (140.6 * x) + 1647.39


# Implementing Newton Raphson Method
def newtonRaphson(x0, e, N, v):
    print('\n\nSOLVING FOR v = %d' % v)

    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0, v) == 0.0:
            print('Divide by zero error!')
            break

        x1 = x0 - f(x0, v) / g(x0, v)
        print('I-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1, v)))
        x0 = x1
        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1, v)) > e

    if flag == 1:
        print('\nRoot is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


# Initial Guess
x0 = 0.01
# Error
e = 0.0001
# Maximum iterations
N = 20

newtonRaphson(x0, e, N, 250)
newtonRaphson(x0, e, N, 500)
