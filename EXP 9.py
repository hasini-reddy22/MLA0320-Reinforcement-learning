import random

# Parameters
MAX_QUEUE = 5
EPISODES = 5000
GAMMA = 0.9

# Agent speeds (probability of resolving call per step)
FAST_AGENT = 0.8
SLOW_AGENT = 0.5


# -----------------------------
# Environment Simulation
# -----------------------------
def step(queue, policy):
    reward = 0

    # New incoming call (probabilistic)
    if random.random() < 0.6:
        queue = min(queue + 1, MAX_QUEUE)

    if queue > 0:
        agent_type = policy(queue)

        if agent_type == "fast":
            success_prob = FAST_AGENT
        else:
            success_prob = SLOW_AGENT

        # Try to resolve call
        if random.random() < success_prob:
            queue -= 1
            reward += 10

    # Waiting penalty
    reward -= queue

    return queue, reward


# -----------------------------
# Policies
# -----------------------------
def random_policy(queue):
    return "fast" if random.random() < 0.5 else "slow"


def fast_first_policy(queue):
    return "fast"


def balanced_policy(queue):
    if queue > 2:
        return "fast"
    return "slow"


# -----------------------------
# Monte Carlo Evaluation
# -----------------------------
def monte_carlo(policy):
    returns_sum = [0.0] * (MAX_QUEUE + 1)
    returns_count = [0] * (MAX_QUEUE + 1)

    for _ in range(EPISODES):
        queue = random.randint(0, MAX_QUEUE)
        episode = []

        # Generate episode
        for t in range(20):
            state = queue
            queue, reward = step(queue, policy)
            episode.append((state, reward))

        # Compute returns (backward)
        G = 0
        visited = set()

        for t in reversed(range(len(episode))):
            state, reward = episode[t]
            G = reward + GAMMA * G

            if state not in visited:
                returns_sum[state] += G
                returns_count[state] += 1
                visited.add(state)

    # Value function
    V = [0.0] * (MAX_QUEUE + 1)
    for s in range(MAX_QUEUE + 1):
        if returns_count[s] > 0:
            V[s] = returns_sum[s] / returns_count[s]

    return V


# -----------------------------
# Run Evaluation
# -----------------------------
random.seed(42)

V_random = monte_carlo(random_policy)
V_fast = monte_carlo(fast_first_policy)
V_balanced = monte_carlo(balanced_policy)

# Print results
print("State Value Function (Queue Size = 0 to 5)\n")

print("Random Policy:   ", [round(v, 2) for v in V_random])
print("Fast-First Policy:", [round(v, 2) for v in V_fast])
print("Balanced Policy: ", [round(v, 2) for v in V_balanced])
