import numpy as np


def main() -> None:
    x = np.tril(np.ones((4, 3)), k=-1)
    print(x)


if __name__ == "__main__":
    main()
