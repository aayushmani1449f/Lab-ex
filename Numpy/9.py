import numpy as np


def main() -> None:
    arr = np.array([10, 20, 30])
    appended = np.append(arr, [40, 50, 60, 70, 80, 90])

    print("Original array:")
    print(arr)
    print("After append values to the end of the array:")
    print(appended)


if __name__ == "__main__":
    main()
