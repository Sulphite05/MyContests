def subsonic_subway(lst):
    max_lower, min_upper = 0, float("inf")
    for i in range(1, len(lst)+1):
        if lst[i-1][1]:
            max_lower = max(max_lower, i / lst[i-1][1])
        if lst[i-1][0]:
            min_upper = min(min_upper, i / lst[i-1][0])

    return max_lower if max_lower <= min_upper else -1


with open("input.txt", "r") as f:
    lines = f.read().split('\n')

with open("output.txt", "w") as f:
    test_cases = int(lines[0])
    k = 1
    for i in range(1, test_cases+1):
        N = int(lines[k])
        lst = []
        # print(N)
        for j in range(N):
            x, y = lines[k+j+1].split()
            lst.append([int(x), int(y)])
        ans = subsonic_subway(lst)
        f.write(f"Case #{i}: {ans}\n")
        # print(lst)
        k += N + 1
