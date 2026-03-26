import numpy as np


def main() -> None:
    x = np.array([1, 2, 3])

    print("Size of the array:", x.size)
    print("Length of one array element in bytes:", x.itemsize)
    print("Total bytes consumed by the elements of the array:", x.nbytes)


if __name__ == "__main__":
    main()
