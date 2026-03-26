import numpy as np


def main() -> None:
    x = np.array([[1, 2, 3], [4, 5, 6]])
    output_file = "numpy_array.txt"

    np.savetxt(output_file, x, fmt="%d", delimiter=" ")
    print(f"Saved array to: {output_file}")
    print(x)


if __name__ == "__main__":
    main()
