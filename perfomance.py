import numpy as np
import matplotlib.pyplot as plt
import timeit

def func_py(x: list[float], N: int) -> list[float]:
    """
    Calculate function values for passed array of arguments
    """
    return [ 1 - ((t - N/2) / (N/2))**2 for t in x ]

def tabulate_py(a: float, b: float, n: int) -> dict[float]:
    N = n
    x = [ a + x*(b - a)/n for x in range(n) ]
    y = func_py(x, N)
    return dict(zip(x, y))

def tabulate_np(a: float, b: float, n: int) -> np.ndarray:
    N = n
    x = np.linspace(a, b, n)
    y = 1 - ((x - N/2) / (N/2))**2
    return np.array([x, y]).T

def main():
    a, b, n = 0, 1, 1000

    n = np.array((1_000, 2_000, 5_000, 10_000, 20_000, 50_000, 100_000), dtype="uint32")
    t_py = np.full_like(n, 0, dtype=float)
    t_np = np.full_like(n, 0, dtype=float)
    for i in range(len(n)):
        t_py[i] = 1_000_000 * timeit.timeit(f"tabulate_py(0, 1, {n[i]})", number=100, globals=globals()) / 100
        t_np[i] = 1_000_000 * timeit.timeit(f"tabulate_np(0, 1, {n[i]})", number=100, globals=globals()) / 100

    plt.plot(n, t_py/t_np)
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()