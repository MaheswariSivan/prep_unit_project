from scipy.optimize import curve_fit
import numpy as np

def set_objective(x, a, b):
    """ return the objective function """
    #To-Do set the objective equation
    return (a * x) + b

def get_result( x, y):
    """Return optimal values for a and b for the equation y = a*x+b """
    x = np.array(x)
    y = np.array(y)
    # curve fit
    try:
        estimations, _ = curve_fit(set_objective, x, y)
    except Exception as e:
        print(f"Error in curve fitting: {e}")
        return None, None
    # summarize the parameter values
    a, b = estimations
    print('y = %.5f * x + %.5f' % (a, b))
    return a,b 
