def solve(arr):
    obj = 1000000
    col0 = [i[0] for i in arr]
    col1 = [i[1] for i in arr]
    col2 = [i[2] for i in arr]
    col3 = [i[3] for i in arr]

    if (min(col0) + min(col1) + min(col2) + min(col3) < obj):
        return [-1, -1, -1, -1]

    c = min(col0)
    if (c >= obj):
        return [1000000, 0, 0, 0]

    m = min(col1)
    if (m >= obj):
        return [1000000, 0, 0, 0]

    y = min(col2)
    if (y >= obj):
        return [1000000, 0, 0, 0]

    k = min(col3)
    if (k >= obj):
        return [1000000, 0, 0, 0]

    res = c

    while res < obj:
        temp_m = 0
        while temp_m < m and res < obj:
            temp_m += 1
            res += 1

        temp_y = 0
        while temp_y < y and res < obj:
            temp_y += 1
            res += 1

        temp_k = 0
        while temp_k < k and res < obj:
            temp_k += 1
            res += 1



    return [c, temp_m, temp_y, temp_k]


if __name__ == "__main__":
    T = int(input())
    
    for t in range(1, T + 1):
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        arr3 = list(map(int, input().split()))

        arr = [arr1, arr2, arr3]
        result = solve(arr)

        print("Case #{}:".format(t), end='')

        if result[0] == -1:
            print(" IMPOSSIBLE")
        else:
            print(' ', end='')
            for n in result:
                print(n, end=' ')
            print()
