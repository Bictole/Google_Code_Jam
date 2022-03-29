def solve(n, arr):
    res = 0
    for i in range(n - 1):
        if arr[i] < arr[i + 1]:
            continue
        if arr[i] >= arr[i + 1] and len(str(arr[i])) == len(str(arr[i + 1])):
            arr[i + 1] = arr[i + 1] * 10
            res += 1
            continue

        k = len(str(arr[i])) - len(str(arr[i + 1]))
            
        if arr[i + 1] * (10**k) > arr[i]:
            arr[i + 1] = arr[i + 1] * (10**k)
            res += k
            continue
        
        test = arr[i + 1]
        for j in range(k):
            test = test * 10 + 9
            
        if test <= arr[i]:
            arr[i + 1] = arr[i + 1] * (10**(k+1))
            res += (k+1)
            continue
        
        arr[i + 1] = arr[i] + 1
        res += k
                
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