import numpy as np


def main() -> None:
    x = np.array([[0, 1], [2, 3], [4, 5]])
    print("Original array elements:")
    print(x)

    as_list = x.tolist()
    print("Array to list:")
    print(as_list)


if __name__ == "__main__":
    main()
