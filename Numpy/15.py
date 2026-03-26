import numpy as np


def main() -> None:
    a = np.array([1, 2])
    b = np.array([4, 5])

    print("a >", b)
    print(a > b)
    print("a >=", b)
    print(a >= b)
    print("a <", b)
    print(a < b)
    print("a <=", b)
    print(a <= b)


if __name__ == "__main__":
    main()
