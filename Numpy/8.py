import numpy as np


def main() -> None:
    list_data = [1, 2, 3, 4, 5, 6, 7, 8]
    tuple_data = ([8, 4, 6], [1, 2, 3])

    list_arr = np.array(list_data)
    tuple_arr = np.array(tuple_data)

    print("List to array:")
    print(list_arr)
    print("Tuple to array:")
    print(tuple_arr)


if __name__ == "__main__":
    main()
