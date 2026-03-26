import numpy as np


def main() -> None:
    x = np.zeros(10)
    print(x)
    x[5] = 11
    print("Update sixth value to 11")
    print(x)


if __name__ == "__main__":
    main()
