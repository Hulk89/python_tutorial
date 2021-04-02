import sys
from collections import namedtuple

INF = 5 * 10 ** 7


def all_equal(l1, l2):
    """
    array 내의 모든 element가 같은지 비교하는 함수. 길이는 같다고 가정한다.
    """
    for i1, i2 in zip(l1, l2):
        if i1 != i2:
            return False
    return True


n_city, n_bus = list(map(int, input().split()))
edges = [[] for _ in range(n_city)]


for i in range(n_bus):
    s, t, w = tuple(map(int, input().split()))
    edges[s-1].append((t-1, w))

cycles = [0 for _ in range(n_city)]
on = [False for _ in range(n_city)]

distances = [INF for _ in range(n_city)]
distances[0] = 0

queue = [0]
cycles[0] = 1
on[0] = True

while True:
    s = queue.pop(0)
    on[s] = False
    for edge in edges[s]:
        t, w = edge
        if distances[t] > distances[s] + w:
            distances[t] = distances[s] + w
            if not on[t]:
                queue.append(t)
                cycles[t] += 1
                on[t] = True
    if max(cycles) >= n_city:
        print(-1)
        sys.exit(0)
    if len(queue) == 0:
        break



for d in distances[1:]:
    if d == INF:
        print(-1)
    else:
        print(d)
