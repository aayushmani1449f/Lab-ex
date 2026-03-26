import numpy as np


def main() -> None:
    x = np.array([[2, 4, 6], [6, 8, 10]], dtype=np.int32)
    x_new = x.astype(np.float64)

    print(x)
    print("Data type of the array x is:", x.dtype)
    print("New Type:", x_new.dtype)
    print(x_new)


if __name__ == "__main__":
    main()
