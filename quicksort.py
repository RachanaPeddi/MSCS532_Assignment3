import random


def randomized_quicksort(arr):
    """Sort an array using Randomized Quicksort."""
    if len(arr) <= 1:
        return arr.copy()

    pivot = random.choice(arr)

    less = [value for value in arr if value < pivot]
    equal = [value for value in arr if value == pivot]
    greater = [value for value in arr if value > pivot]

    return (
        randomized_quicksort(less)
        + equal
        + randomized_quicksort(greater)
    )


def main():
    test_cases = {
        "Random array": [10, 7, 8, 9, 1, 5],
        "Repeated elements": [4, 2, 4, 1, 2, 4, 3],
        "Already sorted": [1, 2, 3, 4, 5, 6],
        "Reverse sorted": [6, 5, 4, 3, 2, 1],
        "Empty array": [],
        "Single element": [42],
    }

    for name, values in test_cases.items():
        result = randomized_quicksort(values)
        print(f"{name}:")
        print(f"  Original: {values}")
        print(f"  Sorted:   {result}")
        print()


if __name__ == "__main__":
    main()