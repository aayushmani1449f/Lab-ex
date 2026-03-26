import numpy as np


def main() -> None:
    array1 = np.array([0, 10, 20, 40, 60, 80])
    array2 = np.array([10, 30, 40, 50, 70])

    unique = np.setxor1d(array1, array2)

    print("Array1:", array1)
    print("Array2:", array2)
    print("Unique values that are in only one (not both) of the input arrays:")
    print(unique)


if __name__ == "__main__":
    main()
