import numpy as np


def main() -> None:
    x = np.array([1.6e-10, 1.6, 1.2e3, 2.35e-1])

    print("Original array elements:")
    print(x)

    np.set_printoptions(precision=3, suppress=True)
    print("Print array values with precision 3:")
    print(x)


if __name__ == "__main__":
    main()
