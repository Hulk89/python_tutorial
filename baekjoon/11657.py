"""
BELLMAN-FORD(G, w, s) pseudo code

INIT-SINGLE-SOURCE(G, s)
for i = 1 to |G.V| -1
    for each edge (u, v) in G.E
        RELAX(u, v, w)
for each edge (u, v) in G.E
    if v.d > u.d + w(u, v)
        return False
return True
"""
import sys

INF = 5 * 10 ** 7

def all_equal(l1, l2):
    """
    array 내의 모든 element가 같은지 비교하는 함수. 길이는 같다고 가정한다.
    """
    for i1, i2 in zip(l1, l2):
        if i1 != i2:
            return False
    return True

# 1. Get inputs and initialize
n_city, n_bus = list(map(int, input().split()))
edges = [(0, 0, 0) for _ in range(n_bus)]
for i in range(n_bus):
    edges[i] = tuple(map(int, input().split()))  # s, t, w

distances = [INF for _ in range(n_city)]
distances[0] = 0


for visit_count in range(n_city):
    prev_distances = distances.copy()

    for e in edges:
        s, t, w = e
        ## source가 INF인 경우에는 업데이트 하지 않는다.
        if distances[s - 1] == INF:
            continue
        distances[t - 1] = min(distances[t - 1], distances[s - 1] + w)

    ## early stop!
    if all_equal(prev_distances, distances):
        break

    if visit_count == n_city - 1:
        print(-1)
        sys.exit(0)

for d in distances[1:]:
    if d == INF:
        print(-1)
    else:
        print(d)
