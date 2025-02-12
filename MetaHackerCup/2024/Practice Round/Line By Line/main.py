def line_by_line(N, P):
    p_inc = P**((N-1)/N)
    return (p_inc - P)*100


with open("input.txt", "r") as f:
    lines = f.read().split('\n')

with open("output.txt", "w") as f:
    test_cases = int(lines[0])
    for i in range(1, test_cases+1):
        N, P = map(int, lines[i].split())
        ans = line_by_line(N, P/100)
        f.write(f"Case #{i}: {ans}\n")
