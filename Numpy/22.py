import numpy as np


def main() -> None:
    x = np.zeros(5)
    x.flags.writeable = False

    print("Test the array is read-only or not:")
    print("Try to change the value of the first element:")
    x[0] = 1


if __name__ == "__main__":
    main()
