# The function is x^3 - x^2 + 2
def func(x, v):
    return (x ** 3) + (70.3 * (x ** 2)) + (1647.39 * x) - (v / 0.0268)


# Derivative of the above function
# which is 3*x^x - 2*x
def derivFunc(x):
    return (3 * (x ** 2)) + (140.6 * x) + 1647.39


# Function to find the root
def newtonRaphson(x, v):
    h = func(x, v) / derivFunc(x)
    while abs(h) >= 0.0001:
        h = func(x, v) / derivFunc(x)

        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h

    print("The value of the root is : ",
          "%.8f" % x)


# Driver program to test above
x0 = 0.1  # Initial values assumed

newtonRaphson(x0, 250)
