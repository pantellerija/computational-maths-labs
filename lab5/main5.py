import pandas as pd

from lab5.io import *
from lab5.methods import *

function = lambda x: np.log(x)

if __name__ == '__main__':
    x_arr = [1, 4, 6, 5, 3, 1.5, 2.5, 3.5]
    y_arr = [0, 1.3862944, 1.7917595, 1.6094379, 1.0986123, 0.4054641, 0.9162907, 1.2527630]
    polynomials = [L, N]
    try:
        io_arr = [read_from_console, read_from_file]
        if (get_func_type()):
            x_arr, y_arr = get_points(function)
        else:
            n, function = io_arr[get_data_source()]()
            x_arr = function[0]
            y_arr = function[1]
        a = get_arg()
        for p in polynomials:
            arg = p(x_arr, y_arr, a)
            # df = pd.DataFrame(list(arg), columns=['f(x)'])
            print(arg)
            graph(x_arr, y_arr, p)
    except ValueError as e:
        print(e)
