import math
import random
from collections.abc import Iterable

import matplotlib.pyplot as plt


def sequence(start: int, size: int) -> Iterable[float]:
    n: int = start
    a = -0.5 * math.log(0.75)  # drift
    b = 0.5 * math.log(3)  # scale
    for i in range(size):
        yield (math.log(n) - math.log(start) + i * a) / b
        if n % 2:
            n = n // 2
        else:
            n = (3 * n + 1) // 2


def main() -> None:
    plt.figure(figsize=(10, 6))
    start_points = [10**500 + random.randint(0, 10**1000) for _ in range(20)]
    size = 5000
    for start in start_points:
        plt.plot(list(sequence(start, size)))
        plt.plot([1.96 * math.sqrt(i) for i in range(size)], color="black")
        plt.plot([-1.96 * math.sqrt(i) for i in range(size)], color="black")

    plt.title("Collatz Sequences")
    plt.ylim(-3 * math.sqrt(size), 3 * math.sqrt(size))
    plt.xlabel("Steps")
    plt.ylabel("Value")
    plt.show()


if __name__ == "__main__":
    random.seed(4)  # for reproducibility
    main()
