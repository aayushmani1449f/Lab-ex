import numpy as np


def main() -> None:
    x = np.array([1 + 0j, 0.70710678 + 0.70710678j])

    print("Original array", x)
    print("Real part of the array:")
    print(x.real)
    print("Imaginary part of the array:")
    print(x.imag)


if __name__ == "__main__":
    main()
