from collections import defaultdict
from math import gcd
from time import time


def fall_in_line(ants):
    N = len(ants)
    if N <= 2:
        return 0  # At most 2 points are always collinear

    min_moves = N - 1  # Start with the worst case

    for i in range(N):
        slope_count = defaultdict(int)
        x1, y1 = ants[i]

        for j in range(N):
            if j != i:
                x2, y2 = ants[j]
                dx = x2 - x1
                dy = y2 - y1

                if dx == 0:
                    slope = ('inf', 0)
                elif dy == 0:
                    slope = (0, 'inf')
                else:
                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g
                    if dx < 0:
                        dx, dy = -dx, -dy
                    slope = (dy, dx)

                slope_count[slope] += 1

        max_collinear = max(slope_count.values(), default=0)
        moves_needed = N - 1 - max_collinear

        min_moves = min(min_moves, moves_needed)
        if min_moves <= (N - 1) // 2:
            break

    return min_moves


with open("input.txt", "r") as f:
    lines = f.read().split('\n')

with open("output.txt", "w") as f:
    start = time()
    test_cases = int(lines[0])
    k = 1
    for i in range(1, test_cases+1):
        N = int(lines[k])
        lst = []
        print(N)
        for j in range(N):
            x, y = lines[k+j+1].split()
            lst.append([int(x), int(y)])
        ans = fall_in_line(lst)
        f.write(f"Case #{i}: {ans}\n")
        f.flush()
        k += N + 1
    end = time()
    print(end - start)
