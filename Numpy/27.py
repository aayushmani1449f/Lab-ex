import numpy as np


def main() -> None:
    arr = np.array([[10, 20, 30], [40, 50, 60]])
    extra_col = np.array([100, 200])

    result = np.column_stack((arr, extra_col))

    print(result)


if __name__ == "__main__":
    main()
