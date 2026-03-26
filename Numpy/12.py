import numpy as np


def main() -> None:
    array1 = np.array([0, 10, 20, 40, 60])
    array2 = np.array([10, 30, 40])

    common = np.intersect1d(array1, array2)

    print("Array1:", array1)
    print("Array2:", array2)
    print("Common values between two arrays:")
    print(common)


if __name__ == "__main__":
    main()
