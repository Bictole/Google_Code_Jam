def give_val(first):
    res = "1"
    
    n = 3
    for i in range(first - 1):
        res = res + ' ' + str(n)
        n += 2 
    
    return res

if __name__ == "__main__":
    T = int(input())
    
    for t in range(1, T + 1):
        first = int(input())
        print(give_val(first))
        arr = list(map(int, input().split()))