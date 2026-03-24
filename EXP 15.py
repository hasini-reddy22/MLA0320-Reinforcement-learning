import random

# Grid definition
GRID = [
    ['A', '.', '.', 'F', '.'],
    ['.', 'G', '.', '.', '.'],
    ['.', '.', '.', 'G', '.'],
    ['.', '.', 'F', '.', '.'],
    ['.', '.', '.', '.', 'F']
]

N_ROWS = len(GRID)
N_COLS = len(GRID[0])
ACTIONS = ['U', 'D', 'L', 'R']
DELTA = {'U': (-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}

# Q-learning parameters
ALPHA = 0.5
GAMMA = 0.9
EPSILON = 0.1
EPISODES = 5000
MAX_STEPS = 50

# Rewards
def reward(state):
    r, c = state
    if GRID[r][c] == 'F':
        return 10
    elif GRID[r][c] == 'G':
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
        if GRID[i][j] == 'A':
            START = (i,j)

# Initialize Q-table
Q = {}
for i in range(N_ROWS):
    for j in range(N_COLS):
        for a in ACTIONS:
            Q[((i,j), a)] = 0.0

# ε-greedy action selection
def choose_action(state):
    if random.random() < EPSILON:
        return random.choice(ACTIONS)
    values = [Q[(state,a)] for a in ACTIONS]
    max_val = max(values)
    best_actions = [a for a,v in zip(ACTIONS, values) if v==max_val]
    return random.choice(best_actions)

# Training loop
for ep in range(EPISODES):
    state = START
    visited_food = set()
    for step in range(MAX_STEPS):
        action = choose_action(state)
        ns = next_state(state, action)
        r = reward(ns)
        
        # Only give reward for first-time food collection
        if GRID[ns[0]][ns[1]] == 'F':
            if ns in visited_food:
                r = -1
            else:
                visited_food.add(ns)
        
        # Q-learning update
        max_q_next = max([Q[(ns,a)] for a in ACTIONS])
        Q[(state, action)] += ALPHA * (r + GAMMA * max_q_next - Q[(state, action)])
        
        # Terminal condition
        if GRID[ns[0]][ns[1]] == 'G':
            break
        state = ns

# Extract policy
policy = [['' for _ in range(N_COLS)] for _ in range(N_ROWS)]
for r in range(N_ROWS):
    for c in range(N_COLS):
        if GRID[r][c] in ['G','F','A']:
            policy[r][c] = GRID[r][c]
        else:
            values = [Q[((r,c), a)] for a in ACTIONS]
            policy[r][c] = ACTIONS[values.index(max(values))]

# Display learned policy
print("Optimal Policy (Directions to Move):\n")
for row in policy:
    print(row)

# Test run
state = START
path = [state]
visited_food = set()
total_reward = 0
for step in range(MAX_STEPS):
    values = [Q[(state,a)] for a in ACTIONS]
    action = ACTIONS[values.index(max(values))]
    ns = next_state(state, action)
    r = reward(ns)
    if GRID[ns[0]][ns[1]] == 'F' and ns not in visited_food:
        visited_food.add(ns)
        total_reward += r
    elif GRID[ns[0]][ns[1]] == 'G':
        total_reward += r
        path.append(ns)
        break
    else:
        total_reward += r
    path.append(ns)
    state = ns

print("\nTest Run Path:", path)
print("Total Reward Collected:", total_reward)
