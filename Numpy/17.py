import numpy as np


def main() -> None:
    arr = np.array([[10, 20, 30], [20, 40, 50]])
    flattened = arr.flatten()

    print("Original array:")
    print(arr)
    print("New flattened array:")
    print(flattened)


if __name__ == "__main__":
    main()
