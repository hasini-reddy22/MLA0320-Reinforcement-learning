import math

# Grid size
N = 5

# Actions
ACTIONS = ['U', 'D', 'L', 'R']
DELTA = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

GAMMA = 0.9
THETA = 1e-4

# Delivery points (terminal states)
goals = [(0, 4), (4, 4)]

# Rewards
def reward(state):
    if state in goals:
        return 50
    return -1


def next_state(state, action):
    x, y = state
    dx, dy = DELTA[action]
    nx, ny = x + dx, y + dy

    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        return state
    return (nx, ny)


# -----------------------------
# Policy Definitions
# -----------------------------

# 1. Random policy
def random_policy(state):
    prob = {}
    for a in ACTIONS:
        prob[a] = 1.0 / len(ACTIONS)
    return prob


# 2. Greedy policy (move toward nearest goal)
def greedy_policy(state):
    if state in goals:
        return {a: 0 for a in ACTIONS}

    best_action = None
    min_dist = float('inf')

    for a in ACTIONS:
        ns = next_state(state, a)
        # Manhattan distance to nearest goal
        dist = min(abs(ns[0] - g[0]) + abs(ns[1] - g[1]) for g in goals)

        if dist < min_dist:
            min_dist = dist
            best_action = a

    prob = {a: 0 for a in ACTIONS}
    prob[best_action] = 1.0
    return prob


# -----------------------------
# Policy Evaluation
# -----------------------------
def policy_evaluation(policy_func):
    V = [[0.0 for _ in range(N)] for _ in range(N)]

    while True:
        delta = 0
        new_V = [[0.0 for _ in range(N)] for _ in range(N)]

        for i in range(N):
            for j in range(N):
                state = (i, j)

                if state in goals:
                    new_V[i][j] = reward(state)
                    continue

                v = 0
                action_probs = policy_func(state)

                for a in ACTIONS:
                    prob = action_probs[a]
                    ns = next_state(state, a)
                    r = reward(ns)

                    v += prob * (r + GAMMA * V[ns[0]][ns[1]])

                new_V[i][j] = v
                delta = max(delta, abs(v - V[i][j]))

        V = new_V

        if delta < THETA:
            break

    return V


# -----------------------------
# Visualization (simple grid print)
# -----------------------------
def print_values(V, title):
    print("\n" + title)
    for row in V:
        for val in row:
            print(f"{val:6.1f}", end=" ")
        print()


# Run evaluations
V_random = policy_evaluation(random_policy)
V_greedy = policy_evaluation(greedy_policy)

# Display results
print_values(V_random, "Value Function (Random Policy)")
print_values(V_greedy, "Value Function (Greedy Policy)")
