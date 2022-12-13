import sys
import json

if __name__ == "__main__":
    path = sys.argv[1]
    folder = sys.argv[2]
    print("############\n")
    print(path)
    print(folder)
    print(path.replace(" ",","))
    print("############\n")
    for n in sys.argv:
        print(n)

    if folder in ['example01','example02']:
        print("OK")
    else:
        print("FAIL")