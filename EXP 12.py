import random

# Grid size
N = 5

# Start and goal
START = (0, 0)
GOAL = (4, 4)

# Actions
ACTIONS = ['U', 'D', 'L', 'R']
DELTA = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

# Parameters
EPISODES = 5000
GAMMA = 0.9
EPSILON = 0.1


def next_state(state, action):
    x, y = state
    dx, dy = DELTA[action]
    nx, ny = x + dx, y + dy

    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        return state  # hit boundary
    return (nx, ny)


def reward(state):
    if state == GOAL:
        return 50
    return -1


# Initialize Q(s,a)
Q = {}
returns = {}

for i in range(N):
    for j in range(N):
        for a in ACTIONS:
            Q[((i, j), a)] = 0.0
            returns[((i, j), a)] = []


# ε-greedy policy
def choose_action(state):
    if random.random() < EPSILON:
        return random.choice(ACTIONS)
    
    # choose best action
    values = [Q[(state, a)] for a in ACTIONS]
    max_val = max(values)
    
    best_actions = [a for a in ACTIONS if Q[(state, a)] == max_val]
    return random.choice(best_actions)


# Generate one episode
def generate_episode():
    episode = []
    state = START

    while state != GOAL:
        action = choose_action(state)
        next_s = next_state(state, action)
        r = reward(next_s)

        episode.append((state, action, r))
        state = next_s

    return episode


# Monte Carlo Control
def monte_carlo_control():
    for ep in range(EPISODES):
        episode = generate_episode()
        G = 0
        visited = set()

        # backward return calculation
        for t in reversed(range(len(episode))):
            state, action, r = episode[t]
            G = r + GAMMA * G

            if (state, action) not in visited:
                returns[(state, action)].append(G)
                Q[(state, action)] = sum(returns[(state, action)]) / len(returns[(state, action)])
                visited.add((state, action))

        if (ep + 1) % 1000 == 0:
            print("Episode:", ep + 1)


# Extract policy
def extract_policy():
    policy = {}

    for i in range(N):
        for j in range(N):
            state = (i, j)
            values = {a: Q[(state, a)] for a in ACTIONS}
            best_action = max(values, key=values.get)
            policy[state] = best_action

    return policy


# Run training
random.seed(42)
monte_carlo_control()

policy = extract_policy()

# Display policy
print("\nOptimal Policy (Drone Directions):\n")
for i in range(N):
    row = []
    for j in range(N):
        if (i, j) == GOAL:
            row.append("G")
        else:
            row.append(policy[(i, j)])
    print(" ".join(row))
