# CJ = X, JC = Y

def solve(arr):
    res = 0
    X = int(arr[0])
    Y = int(arr[1])
    print(arr, X, Y)
    return res

if __name__ == "__main__":
    print("Please enter the number of samples :")
    T = int(input())
    
    for t in range(1, T + 1):
        print("Please enter the list, with format : X Y str")
        arr = list(map(str, input().split()))
        print("Case #{}:".format(t), solve(arr))