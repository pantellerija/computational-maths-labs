import math

from matplotlib.pyplot import plot, show, axis, legend

func1_solution = lambda x: -1 / x


def euler_diff_eq(func, x, y, h, y_el):
    return y + (h / 2) * (func(x, y) + func(x + h / 2, y_el))


def modified_euler(func, y0, x0, n, h, eps=0.01):
    n = int((n - x0) / h)
    x_axis = [x0+i*h for i in range(n+1)]
    y_axis = [y0]
    y_sol_axis = [func1_solution(x0)]
    print("x | y")
    print(x0, y0)
    for i in range(1, n + 1):
        func_val = func(x_axis[i - 1], y0)
        y0_next = func(x_axis[i], y0 + h * func_val)
        y0 = y0 + h / 2 * (func_val + y0_next)
        y_axis.append(y0)
        y_sol_axis.append(func1_solution(x_axis[i]))
        print(f"{round(x_axis[i], 3)} | {round(y_axis[i], 3)}")
    print("---exact solution---")
    print("x | y")
    for i in range(n+1):
        print(f"{round(x_axis[i], 3)} | {round(y_sol_axis[i], 3)}")
    plot(x_axis, y_axis, "r", label="modified euler method")
    plot(x_axis, y_sol_axis, "g", label="y(x)")
    legend()
    show()


def modified_euler_Runge(func, y0, x0, n, h, eps=0.01):
    print("---modified euler method---")
    M = 1
    fy = y0
    while M > eps:
        m = int((n - x0) / h)
        x2_axis = [x0 + i*h for i in range(m+1)]
        y_axis = [fy]
        y_el_axis = [fy]
        y0 = fy
        y_el = fy
        y_sol_axis = [func1_solution(x0)]
        for i in range(1, m+1):
            func_val = func(x2_axis[i-1], y0)
            y_el = y_el + h*func_val
            y0_next = func(x2_axis[i], y_el)
            y0 = y0 + h / 2 * (func_val + y0_next)
            y_el_axis.append(y_el)
            y_axis.append(y0)
            y_sol_axis.append(func1_solution(x2_axis[i]))
        print(f"x_axis: {x2_axis}")
        print(f"y_axis: {y_axis}")
        h /= 2
        M = abs(y_el_axis[-1] - y_axis[-1])
        x_arr = x2_axis
        y_arr = y_axis
        plot(x_arr, y_arr, "r", label="modified euler method")
        plot(x_arr, y_sol_axis, "g", label="y(x)")
        legend()
        show()


def RK4(func, y0, x0, h):
    k1 = h*func(x0, y0)
    k2 = h*func(x0 + h/2, y0 + k1/2)
    k3 = h*func(x0 + h/2, y0 + k2/2)
    k4 = h*func(x0 + h, y0 + k3)
    y0 = y0 + (k1 + 2*k2 + 2*k3 + k4)/6
    return y0


def adams(func, y0, x0, b, h, eps):
    print("---adams method---")
    n = int((b - x0) / h)
    print(n)
    x_axis = [x0+i*h for i in range(n+1)]
    y_axis = [y0]
    y_sol_axis = [0 for i in range(n+1)]
    f_arr = [y0]
    for i in range(1, 5):
        y0 = RK4(func, y0, x_axis[i-1], h)
        f_arr.append(func(x_axis[i], y0))
        y_axis.append(y0)
    f1 = f_arr[1]
    f2 = f_arr[2]
    f3 = f_arr[3]
    f4 = f_arr[4]
    y4 = y_axis[4]
    for i in range(5, n+1):
        df = f4 - f3
        d2f = f4 - 2 * f3 + f2
        d3f = f4 - 3 * f3 + 3 * f2 - f1
        y = y4 + h * f4 + h ** 2 * df / 2 + 5 * h ** 3 * d2f / 12 + 2 * h ** 4 * d3f / 8
        y_axis.append(y)
        f1 = f2
        f2 = f3
        f3 = f4
        f4 = func(x_axis[i], y)
        y4 = y
    print("x | y")
    for i in range(n+1):
        print(f"{round(x_axis[i], 3)} | {round(y_axis[i], 3)}")
    print("---exact solution---")
    print("x | y")
    for i in range(n+1):
        sol = func1_solution(x_axis[i])
        y_sol_axis[i] = sol
        print(f"{round(x_axis[i], 3)} | {round(sol, 3)}")
    plot(x_axis, y_axis, "r", label="adams method")
    plot(x_axis, y_sol_axis, "g", label="y(x)")
    legend()
    show()
