import math
import random
from collections.abc import Iterable

import matplotlib.pyplot as plt

mu = 0.5 * math.log(0.75)  # drift
sigma = 0.5 * math.log(3)  # scale


def raw_sequence(start: int, size: int) -> Iterable[int]:
    x: int = start
    for n in range(size):
        yield x
        if x % 2:
            x = (3 * x + 1) // 2
        else:
            x = x // 2


def sequence(start: int, size: int) -> Iterable[float]:
    for n, x in enumerate(raw_sequence(start, size)):
        yield math.log(x) - math.log(start) - n * mu


def simple_plot() -> None:
    plt.figure(figsize=(10, 6))
    size = 10
    plt.plot(list(raw_sequence(10, size)), marker="o")
    plt.title("Hailstone numbers")
    plt.xlabel("$t$")
    plt.ylabel("$x_t$")
    plt.grid()
    plt.savefig("hailstone1.png")


def main() -> None:
    plt.figure(figsize=(10, 6))
    start_points = [10**500 + random.randint(0, 10**1000) for _ in range(20)]
    size = 300
    for start in start_points:
        plt.plot(list(sequence(start, size)))

    plt.plot(
        [1.96 * sigma * math.sqrt(i) for i in range(size)],
        color="black",
        linestyle="dashed",
        label="$\\pm 1.96\\sigma\\sqrt{t}$",
    )
    plt.plot(
        [-1.96 * sigma * math.sqrt(i) for i in range(size)],
        color="black",
        linestyle="dashed",
    )
    plt.legend()

    plt.title("Hailstone numbers")
    plt.ylim(-3 * sigma * math.sqrt(size), 3 * sigma * math.sqrt(size))
    plt.xlabel("$t$")
    plt.ylabel("$\\log x_t-\\log x_0 - \\mu t$")
    plt.grid()
    plt.savefig("hailstone2.png")


if __name__ == "__main__":
    simple_plot()
    random.seed(8)  # for reproducibility
    main()
