import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt

def load_history_data(fname: str) -> np.ndarray:
    from_strdate = lambda x: datetime.strptime(x.strip('"'), '%m/%d/%Y')
    from_strnum = lambda x: float(x.strip('"'))
    from_strnumm = lambda x: float(x.strip('"').strip('M'))*1_000_000
    from_strpcnt = lambda x: float((x.strip('"').strip('%')))/100
    names=("date", "price", "open", "high", "low", "volume", "change")
    data = np.genfromtxt(fname, delimiter=",", encoding="utf-8", skip_header=1, names=names,
                         dtype=[("date", datetime),
                                ("price", np.float64),
                                ("open", np.float64),
                                ("high", np.float64),
                                ("low", np.float64),
                                ("volume", np.float64),
                                ("change", np.float64)],
                         converters={
                             "date": from_strdate,
                             "price": from_strnum,
                             "open": from_strnum,
                             "high": from_strnum,
                             "low": from_strnum,
                             "volume": from_strnumm,
                             "change": from_strpcnt})
    return data

def generate_y_values(n: int) -> np.ndarray:
    x = np.linspace(0, n, n+1)
    y = 1 - ((x - n/2) / (n/2)) ** 2
    return y

def plot_history_data(data: np.ndarray, n=100) -> None:
    plt.style.use('dark_background')
    # Generate y-values for the example function
    x = np.linspace(0, n, n+1)
    y_example = generate_y_values(n)

    # Plot the high and low values per last n days (array is reversed in time)
    fig, ax = plt.subplots()
    date, highs, lows = data['date'][:n], data['high'][:n], data['low'][:n]
    ax.plot(date, highs, c='red', alpha=0.5)
    ax.plot(date, lows, c='blue', alpha=0.5)
    plt.fill_between(date, highs, lows, facecolor='blue', alpha=0.1)

    # Add the example function plot
    ax.plot(date, y_example, c='green', alpha=0.5, label='Example Function')

    # Format plot.
    plt.title(f"Stock high and low prices per {n} days with example function", fontsize=18)
    plt.xlabel('', fontsize=12)
    fig.autofmt_xdate()
    plt.ylabel("Price (USD)", fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=12)

    plt.grid()
    plt.legend()
    plt.show()

def main() -> None:
    fname = 'data/AAPL Historical Data.csv'
    data = load_history_data(fname)
    plot_history_data(data)

if __name__ == "__main__":
    main()
