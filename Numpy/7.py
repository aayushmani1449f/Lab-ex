import numpy as np


def main() -> None:
    idx = np.indices((8, 8))
    checkerboard = (idx[0] + idx[1]) % 2
    print(checkerboard)


if __name__ == "__main__":
    main()
