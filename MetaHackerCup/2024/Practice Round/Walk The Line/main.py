def walk_the_line(N, S, mini):
    if N == 1: ans = mini
    else: ans = ((N-1) * 2 - 1) * mini
    return "YES" if ans <= S else "NO"


with open("input.txt", "r") as f:
    lines = f.read().split('\n')

with open("output.txt", "w") as f:
    test_cases = int(lines[0])
    k = 1
    for i in range(1, test_cases+1):
        N, S = map(int, lines[k].split())
        mini = min(map(int, (lines[k+1:k+N+1])))
        ans = walk_the_line(N, S, mini)
        f.write(f"Case #{i}: {ans}\n")
        k += N + 1

