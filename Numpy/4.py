import numpy as np


def main() -> None:
    arr = np.arange(12, 38)
    reversed_arr = arr[::-1]

    print("Original array:")
    print(arr)
    print("Reverse array:")
    print(reversed_arr)


if __name__ == "__main__":
    main()
