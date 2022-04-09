def solve(str):
    res = str
    i = 0
    length = len(res)
    while i < length - 1:
        if (res[i] < res[i + 1]):
            res = res[:i] + res[i] + res[i:]
            i += 1
            length += 1

        if (res[i] == res[i + 1]):
            j = i
            same = True
            while same and j < length - 1:
                if res[j] != res[j + 1]:
                    same = False
                j += 1

            if same:
                return res

            res = res[:i] + res[i] + res[i:]
            i += 1
            length += 1

        i += 1
    return res

if __name__ == "__main__":
    T = int(input())
    
    for t in range(1, T + 1):
        str = input()
        print("Case #{}:".format(t), solve(str))