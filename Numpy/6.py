import numpy as np


def main() -> None:
    original = np.ones((3, 3))
    padded = np.pad(original, pad_width=1, mode="constant", constant_values=0)

    print("Original array:")
    print(original)
    print("1 on the border and 0 inside in the array")
    print(padded)


if __name__ == "__main__":
    main()
