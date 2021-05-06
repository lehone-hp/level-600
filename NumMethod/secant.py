import matplotlib.pyplot as plt
import numpy as np


# define the function to investigate
def f(x):
    return (x ** 3) + (70.3 * x ** 2) + (1647.39 * x) - (v / 0.0268)


# and its derivative
def fp(x):
    return (3 * x ** 2) + (140.6 * x) + 1647.39


# loop over all starting points defined in pointlist
for x0 in pointlist:
    # set desired precision and max number of iterations
    prec_goal = 1.e-10
    nmax = 1000
    # initialize values for iteration loop
    reldiff = 1
    xi = x0
    counter = 0
    # start iteration loop
    while reldiff > prec_goal and counter < nmax:
        #        # plot the tangents, points and intersections for finding the next xi
        #        # plot star on the curve where x=xi
        #        plt.plot(xi,f(xi),'r*', markersize=16)
        #        # compute y values for tangent plotting
        #        tangy = fp(xi)*xvals + f(xi) - fp(xi)*xi
        #        # plot the tangent
        #        plt.plot(xvals, tangy, 'r--')
        #        # perfom iteration step and compute next xi
        #        x1 = xi - f(xi)/fp(xi)
        #        # print numbers for use in convergence tables (csv format)
        #        print('%i, %15.12f, %15.12f, %15.12f' % (counter+1, x1, np.abs(f(xi)/fp(xi)), np.abs(f(xi)/fp(xi)/xi)))
        #        # plot next xi on the axis
        #        plt.plot(x1,0,'gx', markersize=16)
        #        # trade value to next iteration step
        #        xi = x1

        # get the number of necessary iterations at that particular x0
        # compute relative difference
        reldiff = np.abs(f(xi) / fp(xi) / xi)
        # compute next xi
        x1 = xi - f(xi) / fp(xi)
        # trade output to input for next iteration step
        xi = x1
        # increase counter
        counter += 1

    # plot the number of necessary iterations at that particular x0
    plt.plot(x0, counter, 'r.', markersize=5)
    # print test output
    print(x0, counter, reldiff)

# save the figure to an output file
plt.savefig('newton-method-demo-figure.jpg', bbox_inches='tight')

# close plot for suppressing the figure output at runtime. Figure is still saved to file
# plt.close()