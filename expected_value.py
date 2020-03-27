import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    r = list(map(int, sys.stdin.readline().strip().split()))
    l = list(map(int, sys.stdin.readline().strip().split()))
    print(r, l)
    total, exp = 1, 0
    map = {}
    for index in range(n):
        for num in range(r[index], l[index]):
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
        total *= (l[index] - r[index] + 1)

    for num in map.keys():
        print(total, num, map[num])
        exp += num * map[num] / total
    print(exp)
            
