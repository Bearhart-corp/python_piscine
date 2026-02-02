import sys
import math


class NumberArgError(Exception):
    def __init__(self):
        super().__init__("Not enough args provided.")


def main():
    print("=== Game Coordinate System ===")
    len_arg: tuple = len(sys.argv)
    coor = sys.argv[1:]
    try:
        coor = [int(x) for x in coor]
        if len_arg < 4:
            raise NumberArgError
    except NumberArgError as e:
        print(e)
        return
    except ValueError as e:
        print(e)
        return
    print(f"Position created: ({coor[0]}, "
          f"{coor[1]}, {coor[2]})")
    value = math.sqrt((coor[0] - 0)**2 + (coor[1] - 0)**2 + (coor[2] - 0)**2)
    print(f"distance between (0, 0, 0) and {coor}: {value}")


if __name__ == "__main__":
    main()
