import math

from matplotlib.pyplot import plot, show, axis, legend

func1_solution = lambda x: -1/x


def euler_diff_eq(func, x, y, h):
    return y + h/2*(func(x, y) + func(x + h/2, y + h*func(x, y)))


def modified_euler(func, y0, x0, n,  h, eps=0.01):
    print("---modified euler method---")
    M = 1
    x_axis = [x0]
    y_axis = [y0]
    y_sol_axis = [func1_solution(x0)]
    print("x | y")
    print(x0, y0)
    while M > eps:
        y = euler_diff_eq(func, x0, y0, h)
        x0 = x0 + h/2
        y_axis.append(y)
        x_axis.append(x0)
        print(f"{round(x0, 3)}: {round(y, 3)}")
        M = abs(y - y0)
        y0 = y
    print("---exact solution---")
    print("x | y")
    for i in range(1, len(x_axis)):
        sol = func1_solution(x_axis[i])
        y_sol_axis.append(sol)
        print(f"{round(x_axis[i], 3)}:  {round(sol, 3)}")
    plot(x_axis, y_axis, "r", label="modified euler method")
    plot(x_axis, y_sol_axis, "g", label="y(x)")
    axis([min(x_axis), n, min(y_axis), max(y_axis)])
    legend()
    show()


def adams(func, y0, x0, b, h, eps):
    print("---adams method---")
    n = int(abs(b - x0) / h)
    x_axis = [x0+i*h for i in range(n)]
    y_axis = [y0]
    f_arr = [0]
    M = 1
    y_sol_axis = [0 for i in range(n)]
    for i in range(1, 5):
        y0 = euler_diff_eq(func, x_axis[i], y0, h)
        f_arr.append(func(x_axis[i], y0))
        y_axis.append(y0)
    f1 = f_arr[1]
    f2 = f_arr[2]
    f3 = f_arr[3]
    f4 = f_arr[4]
    y4 = y_axis[4]
    for i in range(5, n):
        df = f4 - f3
        d2f = f4-2*f3+f2
        d3f = f4-3*f3+3*f2-f1
        y = y4 + h*f4 + h**2*df/2 + 5*h**3*d2f/12 + 2*h**4*d3f/8
        y_axis.append(y)
        M = abs(y-y4)/15
        f1 = f2
        f2 = f3
        f3 = f4
        f4 = func(x_axis[i], y)
        y4 = y
    print("x | y")
    for i in range(n):
        print(f"{round(x_axis[i], 3)} | {round(y_axis[i], 3)}")
    print(f"accuracy estimate at the last step: {round(M, 3)}")
    print("---exact solution---")
    print("x | y")
    for i in range(n):
        sol = func1_solution(x_axis[i])
        y_sol_axis[i] = sol
        print(f"{round(x_axis[i], 3)} | {round(sol, 3)}")
    plot(x_axis, y_axis, "r", label="adams method")
    plot(x_axis, y_sol_axis, "g", label="y(x)")
    legend()
    show()

