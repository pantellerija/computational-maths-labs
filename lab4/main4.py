import approx as ap

if __name__ == '__main__':
    func = [[1.2, 2.9, 4.1, 5.5, 6.7, 7.8, 9.2, 10.3],
            [7.4, 9.5, 11.1, 12.9, 14.6, 17.3, 18.2, 20.7]]
    func2 = [[1.1, 2.3, 3.7, 4.5, 5.4, 6.8, 7.5],
             [2.5, 4.1, 5.2, 6.9, 8.3, 14.8, 21.2]]
    app_func, e_arr, p_arr, s = ap.quad_approx(func2)