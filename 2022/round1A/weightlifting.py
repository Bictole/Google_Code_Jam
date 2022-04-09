def solve(E, W, exercices):
    res = 0
    
    return res

if __name__ == "__main__":
    T = int(input())
    
    for t in range(1, T + 1):
        arr = list(map(int, input().split()))
        E = arr[0]
        W = arr[1]

        exercices = []
        for i in range(E):
            ex = list(map(int, input().split()))
            exercices.append(ex)

    print("Case #{}:".format(t), solve(E, W, exercices))
