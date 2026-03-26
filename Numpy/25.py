import numpy as np


def main() -> None:
    x = np.array(
        [
            0.26153123,
            0.52760141,
            0.5718299,
            0.5927067,
            0.7831874,
            0.69746349,
            0.35399976,
            0.99469633,
            0.0694458,
            0.54711478,
        ]
    )

    print("Original array elements:")
    print(x)

    np.set_printoptions(precision=3, suppress=True)
    print("Print array values with precision 3:")
    print(x)


if __name__ == "__main__":
    main()
