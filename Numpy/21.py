import numpy as np


def main() -> None:
    arr1 = np.array([[0, 1, 3], [5, 7, 9]])
    arr2 = np.array([[0, 2, 4], [6, 8, 10]])
    concatenated = np.concatenate((arr1, arr2), axis=1)

    print(concatenated)


if __name__ == "__main__":
    main()
