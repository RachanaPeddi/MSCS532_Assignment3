import random
import time
import sys

from quicksort import randomized_quicksort


# Increase the recursion limit so deterministic Quicksort
# can be tested on sorted and reverse-sorted inputs.
sys.setrecursionlimit(10000)


def deterministic_quicksort(arr):
    """Sort using the first element as the pivot."""
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[0]

    less = [value for value in arr if value < pivot]
    equal = [value for value in arr if value == pivot]
    greater = [value for value in arr if value > pivot]

    return (
        deterministic_quicksort(less)
        + equal
        + deterministic_quicksort(greater)
    )


def measure_time(sort_function, data, trials=5):
    """Return the average execution time over several trials."""
    total_time = 0.0

    for _ in range(trials):
        test_data = data.copy()

        start = time.perf_counter()
        result = sort_function(test_data)
        end = time.perf_counter()

        # Verify that the algorithm produced the correct result.
        assert result == sorted(data)

        total_time += end - start

    return total_time / trials


def create_test_data(size, distribution):
    """Create input data for a specified distribution."""
    if distribution == "Random":
        return [random.randint(0, size * 10) for _ in range(size)]

    if distribution == "Sorted":
        return list(range(size))

    if distribution == "Reverse Sorted":
        return list(range(size, 0, -1))

    if distribution == "Repeated Elements":
        return [random.randint(1, 10) for _ in range(size)]

    raise ValueError("Unknown distribution")


def main():
    sizes = [100, 500, 1000, 2000]

    distributions = [
        "Random",
        "Sorted",
        "Reverse Sorted",
        "Repeated Elements",
    ]

    print("Randomized vs. Deterministic Quicksort")
    print("Average execution time over 5 trials")
    print()

    header = (
        f"{'Distribution':<20}"
        f"{'Size':>8}"
        f"{'Randomized (s)':>18}"
        f"{'Deterministic (s)':>22}"
    )

    print(header)
    print("-" * len(header))

    for distribution in distributions:
        for size in sizes:
            data = create_test_data(size, distribution)

            randomized_time = measure_time(
                randomized_quicksort, data
            )

            deterministic_time = measure_time(
                deterministic_quicksort, data
            )

            print(
                f"{distribution:<20}"
                f"{size:>8}"
                f"{randomized_time:>18.6f}"
                f"{deterministic_time:>22.6f}"
            )

        print()


if __name__ == "__main__":
    main()