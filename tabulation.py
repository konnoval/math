import numpy as np
from matplotlib import pyplot as plt

def func_py(x: np.ndarray) -> np.ndarray:
    """
    Calculate function values for passed array of arguments
    """
    return x / (x**2 + 1)

def tabulate_py(a: float, b: float, n: int) -> np.ndarray:
    x = np.linspace(a, b, n)
    y = func_py(x)
    return np.array([x, y]).T

def tabulate_np(a: float, b: float, n: int) -> np.ndarray:
    x = np.linspace(a, b, n)
    y = func_py(x)
    return np.array([x, y]).T

def test_tabulation(f, a, b, n, axis):
    res = f(a, b, n)

    axis.plot(res[:, 0], res[:, 1], label=f.__name__)
    axis.grid()
    axis.legend()

def main():
    a, b, n = 0, 1, 1000

    fig, (ax1, ax2) = plt.subplots(2, 1)
    test_tabulation(tabulate_py, a, b, n, ax1)
    test_tabulation(tabulate_np, a, b, n, ax2)
    plt.show()

if __name__ == '__main__':
    main()
