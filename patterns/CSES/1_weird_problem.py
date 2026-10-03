import sys

control = []

def weird_func(n: int):
    if not control:
        control.append(str(n))

    if n == 1:
        return 


    elif n % 2 == 0:
        value = n / 2
        control.append(str(int(value)))
        weird_func(value)


    else:
        value = (n * 3) + 1
        control.append(str(int(value)))
        weird_func(value)


if __name__ == "__main__":


    # print(sys.stdin.readline())a

    # weird_func(int(sys.argv[1]))
    weird_func(int(sys.stdin.readline()))
    print(" ".join(control))


