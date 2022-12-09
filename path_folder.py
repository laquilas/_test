import sys


if __name__ == "__main__":
    path = sys.argv[1]
    folder = sys.argv[2]

    if folder in ['example01','example02']:
        print("OK")
    else:
        print("FAIL")