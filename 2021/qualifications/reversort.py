def solve(n, arr):
    res = 0
    for i in range(n - 1):
        mini = min(arr[i:])
        j = arr.index(mini) + 1
        arr[i:j] = reversed(arr[i:j])
        res += j - i
    return res

if __name__ == "__main__":
    print("Please enter the number of samples :")
    T = int(input())
    
    for t in range(1, T + 1):
        print("Please enter the number of elements in the following list :")
        n = int(input())
        print("Please enter the list, with format : 1 2 3 4 5")
        arr = list(map(int, input().split()))
        print("Case #{}:".format(t), solve(n, arr))