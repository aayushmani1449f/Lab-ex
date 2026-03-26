import numpy as np


def main() -> None:
    arr = np.arange(12).reshape(3, 4)
    new_arr = arr * 3

    print("Original array elements:")
    print(arr)
    print("New array elements:")
    print(new_arr)


if __name__ == "__main__":
    main()
