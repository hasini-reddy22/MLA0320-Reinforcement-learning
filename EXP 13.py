import random

# Maze setup
MAZE = [
    ['S', '.', '.', '.', '.'],
    ['.', 'T', '.', 'T', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', 'T', '.', '.', '.'],
    ['.', '.', '.', 'T', 'G']
]

N_ROWS = len(MAZE)
N_COLS = len(MAZE[0])

ACTIONS = ['U', 'D', 'L', 'R']
DELTA = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

# Parameters
ALPHA = 0.1
GAMMA = 0.9
EPISODES = 5000
EPSILON = 0.1

# Rewards
def reward(state):
    r, c = state
    if MAZE[r][c] == 'G':
        return 50
    elif MAZE[r][c] == 'T':
        return -50
    else:
        return -1

# Next state (handle boundaries)
def next_state(state, action):
    r, c = state
    dr, dc = DELTA[action]
    nr, nc = r + dr, c + dc
    if 0 <= nr < N_ROWS and 0 <= nc < N_COLS:
        return (nr, nc)
    return state

# Find start position
for i in range(N_ROWS):
    for j in range(N_COLS):
        if MAZE[i][j] == 'S':
            START = (i, j)
        if MAZE[i][j] == 'G':
            GOAL = (i, j)

# Initialize value function
V = [[0.0 for _ in range(N_COLS)] for _ in range(N_ROWS)]

# ε-greedy policy based on current V
def choose_action(state):
    if random.random() < EPSILON:
        return random.choice(ACTIONS)
    # greedy: pick action leading to max V
    values = []
    for a in ACTIONS:
        ns = next_state(state, a)
        values.append(V[ns[0]][ns[1]])
    max_val = max(values)
    best_actions = [a for a, v in zip(ACTIONS, values) if v == max_val]
    return random.choice(best_actions)

# TD(0) Learning
for ep in range(EPISODES):
    state = START
    while state != GOAL and MAZE[state[0]][state[1]] != 'T':
        action = choose_action(state)
        ns = next_state(state, action)
        r = reward(ns)
        # TD(0) update
        V[state[0]][state[1]] += ALPHA * (r + GAMMA * V[ns[0]][ns[1]] - V[state[0]][state[1]])
        state = ns

# Display learned value function
print("State-Value Function after TD(0):\n")
for row in V:
    print(["{0:6.2f}".format(v) for v in row])

# Extract policy (greedy based on V)
policy = [['' for _ in range(N_COLS)] for _ in range(N_ROWS)]
for r in range(N_ROWS):
    for c in range(N_COLS):
        if MAZE[r][c] in ['G', 'T']:
            policy[r][c] = MAZE[r][c]
        else:
            values = []
            for a in ACTIONS:
                ns = next_state((r,c), a)
                values.append(V[ns[0]][ns[1]])
            best_a = ACTIONS[values.index(max(values))]
            policy[r][c] = best_a

print("\nDerived Policy (Directions to Move):\n")
for row in policy:
    print(row)
