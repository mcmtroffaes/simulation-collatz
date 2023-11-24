import math
import random
from collections.abc import Iterable

import matplotlib.pyplot as plt


def sequence(start: int, size: int) -> Iterable[float]:
    x: int = start
    alpha = -0.5 * math.log(0.75)  # drift
    beta = 0.5 * math.log(3)  # scale
    for n in range(size):
        yield (math.log(x) - math.log(start) + n * alpha) / beta
        if x % 2:
            x = x // 2
        else:
            x = (3 * x + 1) // 2


def main() -> None:
    plt.figure(figsize=(10, 6))
    start_points = [10**500 + random.randint(0, 10**1000) for _ in range(20)]
    size = 5000
    for start in start_points:
        plt.plot(list(sequence(start, size)))

    plt.plot([1.96 * math.sqrt(i) for i in range(size)], color="black", linestyle='dashed', label="$\\pm 1.96\\sqrt{n}$")
    plt.plot([-1.96 * math.sqrt(i) for i in range(size)], color="black", linestyle='dashed')
    plt.legend()

    plt.title("Collatz Sequences")
    plt.ylim(-3 * math.sqrt(size), 3 * math.sqrt(size))
    plt.xlabel("$n$")
    plt.ylabel("$(\\log x_n-\\log x_0+ \\alpha n)/\\beta$")
    plt.show()


if __name__ == "__main__":
    random.seed(4)  # for reproducibility
    main()
