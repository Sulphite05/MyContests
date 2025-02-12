def line_of_delivery(G, lst):
    for i in range(1, len(lst)):
        if lst[i] >= lst[i-1]:
            num = lst[i] - lst[i-1] + 1
            lst[i] = lst[i-1] - 1
            j = i - 1
            while num > 0:
                if j == 0 or lst[j] + num < lst[j-1]:
                    lst[j] += num
                    break

                diff = lst[j-1] - lst[j] - 1

                if diff > 0:
                    lst[j] = lst[j - 1] - 1
                    num -= diff

                j -= 1

    left, right = 0, len(lst) - 1
    while left < right - 1:
        mid = (left + right)//2
        if lst[mid] == G:
            return mid+1, 0
        if G > lst[mid]:
            right = mid
        else:
            left = mid

    ans = left if abs(lst[left] - G) <= abs(lst[right] - G) else right
    return ans + 1, abs(lst[ans] - G)


with open("input.txt", "r") as f:
    lines = f.read().split('\n')

with open("output.txt", "w") as f:
    test_cases = int(lines[0])
    k = 1
    for i in range(1, test_cases+1):
        N, G = map(int, lines[k].split())
        lst = list(map(int, (lines[k+1:k+N+1])))
        ans = line_of_delivery(G, lst)
        f.write(f"Case #{i}: {ans[0]} {ans[1]}\n")
        f.flush()
        k += N + 1

