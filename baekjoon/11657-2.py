import sys

INF = 5 * 10 ** 7

# 1.  Get inputs  
n_city, n_bus = list(map(int, input().split()))
edges = [[] for _ in range(n_city)]

for i in range(n_bus):
    s, t, w = tuple(map(int, input().split()))
    edges[s-1].append((t-1, w))

# 2. Initialization

number_of_visits = [0 for _ in range(n_city)]
check_in_queue = [False for _ in range(n_city)]
distances = [INF for _ in range(n_city)]
queue = []

distances[0] = 0
# NOTE: push operation is composed of these 3 actions.
queue.append(0)
number_of_visits[0] += 1
check_in_queue[0] = True

# 3. Run
while queue:
    # NOTE: pop operation is composed of these 2 actions.
    s = queue.pop(0)
    check_in_queue[s] = False

    for edge in edges[s]:
        t, w = edge
        if distances[t] > distances[s] + w:
            distances[t] = distances[s] + w
            if not check_in_queue[t]:
                queue.append(t)
                number_of_visits[t] += 1
                check_in_queue[t] = True
    
    if max(number_of_visits) >= n_city:
        print(-1)
        sys.exit(0)

for d in distances[1:]:
    if d == INF:
        print(-1)
    else:
        print(d)
