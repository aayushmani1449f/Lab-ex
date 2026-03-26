import numpy as np


def main() -> None:
    original_list = [12.23, 13.32, 100, 36.32]
    arr = np.array(original_list)

    print("Original List:", original_list)
    print("One-dimensional numpy array:", arr)


if __name__ == "__main__":
    main()
