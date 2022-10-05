from lab6.io import get_float, get_method_type
from lab6.methods import modified_euler, adams, modified_euler_Runge

# b = 1.5 y0 = -1 x0 = 1 h = .1 eps = .01
func = lambda x, y: y + (1+x)*y*y

methods = [modified_euler, modified_euler_Runge, adams]

if __name__ == '__main__':
    print("diff eq: y'(x) = y + (1+x)*y^2")
    # b = get_float("enter the right boundary of the interval: ")
    # x0 = get_float("enter x0: ")
    # y0 = get_float("enter y(x0): ")
    # h = get_float("enter h: ")
    # eps = get_float("enter epsilon: ")
    methods[1](func, -1, 1, 1.5, 0.1, 0.01)
