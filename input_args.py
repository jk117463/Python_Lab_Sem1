import sys

if __name__ == '__main__':
    print(sys.argv)
    print(sys.argv[1])
    print(sys.argv[1])
    for arg in sys.argv:
        print(arg)
        print(type(arg))