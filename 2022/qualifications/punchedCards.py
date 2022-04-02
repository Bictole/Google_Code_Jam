def solve(arr):
    R = arr[0]
    C =arr[1]

    limiter = True
    firstLine = True
    secondLine = False

    for i in range(2 * R + 1):
        if limiter:
            limiter = False
            if firstLine:
                print("..", end='')
                firstLine = False
                secondLine = True

                for j in range(C - 1):
                    print("+-", end='')

                print("+")
                continue

            for j in range(C):
                    print("+-", end='')
            print("+")
        else:
            limiter = True
            if  secondLine:
                print("..", end='')
                firstLine = False
                secondLine = False

                for j in range(C - 1):
                    print("|.", end='')

                print("|")
                continue

            for j in range(C):
                    print("|.", end='')
            print("|")


if __name__ == "__main__":
    T = int(input())
    
    for t in range(1, T + 1):
        arr = list(map(int, input().split()))
        print("Case #{}:".format(t))
        solve(arr)