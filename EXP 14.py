import random

# Environment setup (5x5 house)
HOUSE = [
    ['S', '.', '.', 'O', '.'],
    ['.', 'O', '.', 'O', '.'],
    ['.', '.', '.', '.', '.'],
    ['O', '.', 'O', '.', '.'],
    ['.', '.', '.', 'O', '.']
]

N_ROWS = len(HOUSE)
N_COLS = len(HOUSE[0])

ACTIONS = ['U', 'D', 'L', 'R']
DELTA = {'U': (-1,0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}

# Parameters
ALPHA = 0.5
GAMMA = 0.9
EPSILON = 0.1
EPISODES = 5000
MAX_STEPS = 50

# Find starting position
for i in range(N_ROWS):
    for j in range(N_COLS):
        if HOUSE[i][j] == 'S':
            START = (i,j)

# Initialize Q-values
Q = {}
for i in range(N_ROWS):
    for j in range(N_COLS):
        for a in ACTIONS:
            Q[((i,j), a)] = 0.0

# ε-greedy policy
def choose_action(state):
    if random.random() < EPSILON:
        return random.choice(ACTIONS)
    values = [Q[(state, a)] for a in ACTIONS]
    max_val = max(values)
    best_actions = [a for a, v in zip(ACTIONS, values) if v == max_val]
    return random.choice(best_actions)

# Next state
def next_state(state, action):
    r, c = state
    dr, dc = DELTA[action]
    nr, nc = r + dr, c + dc
    if 0 <= nr < N_ROWS and 0 <= nc < N_COLS:
        if HOUSE[nr][nc] != 'O':
            return (nr, nc)
    return state

# Reward function
def reward(state, cleaned):
    r, c = state
    if HOUSE[r][c] == 'O':
        return -5
    elif state not in cleaned:
        return 10
    else:
        return -1

# SARSA algorithm
for ep in range(EPISODES):
    state = START
    cleaned = set()
    action = choose_action(state)

    for step in range(MAX_STEPS):
        next_s = next_state(state, action)
        r = reward(next_s, cleaned)
        if r == 10:  # cleaned new tile
            cleaned.add(next_s)
        next_a = choose_action(next_s)

        # SARSA update
        Q[(state, action)] += ALPHA * (r + GAMMA * Q[(next_s, next_a)] - Q[(state, action)])
        state, action = next_s, next_a

# Extract policy
policy = [['' for _ in range(N_COLS)] for _ in range(N_ROWS)]
for r in range(N_ROWS):
    for c in range(N_COLS):
        if HOUSE[r][c] == 'O':
            policy[r][c] = 'O'
        else:
            values = [Q[((r,c), a)] for a in ACTIONS]
            policy[r][c] = ACTIONS[values.index(max(values))]

# Display learned policy
print("\nOptimal Cleaning Policy:\n")
for row in policy:
    print(row)
