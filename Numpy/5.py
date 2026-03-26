import numpy as np


def main() -> None:
    original = np.ones((5, 5))
    arr = original.copy()
    arr[1:-1, 1:-1] = 0

    print("Original array:")
    print(original)
    print("1 on the border and 0 inside in the array")
    print(arr)


if __name__ == "__main__":
    main()
