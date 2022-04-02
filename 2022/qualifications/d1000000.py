def solve(n, arr):
    res = 0

    for i in range(n):
        mini = min(arr)
        arr.remove(mini)

        if mini > res:
            res += 1
        else:
            continue

    return res


if __name__ == "__main__":
    T = int(input())
    
    for t in range(1, T + 1):
        n = int(input())
        arr = list(map(int, input().split()))
        print("Case #{}:".format(t), solve(n, arr))