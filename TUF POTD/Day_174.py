import sys
from bisect import bisect_left
from collections import defaultdict

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & -i
        return result

def main():
    input = sys.stdin.readline
    q, D = map(int, input().split())
    reports = [tuple(map(int, input().split())) for _ in range(q)]

    temps = sorted(set(temp for _, temp in reports))
    ranks = {temp: i + 1 for i, temp in enumerate(temps)}

    bit = FenwickTree(len(temps))
    latest = {}
    output = []

    for station, temp in reports:
        if station in latest:
            old_temp = latest[station]

            if abs(temp - old_temp) > D:
                count = bit.query(bisect_left(temps, temp))
                if old_temp < temp:
                    count -= 1
                output.append(f"{station} {temp} {count}")

            bit.update(ranks[old_temp], -1)

        latest[station] = temp
        bit.update(ranks[temp], 1)

    print("\n".join(output))

if __name__ == "__main__":
    main()