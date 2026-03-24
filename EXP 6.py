import random
import math

# True click probabilities for ads (unknown to algorithm)
true_ctr = [0.05, 0.08, 0.12, 0.04, 0.10]
n_arms = len(true_ctr)

T = 10000  # number of rounds


def simulate_reward(arm):
    if random.random() < true_ctr[arm]:
        return 1
    return 0


# -----------------------------
# 1. Epsilon-Greedy
# -----------------------------
def epsilon_greedy(epsilon=0.1):
    counts = [0] * n_arms
    values = [0.0] * n_arms
    total_reward = 0

    for t in range(T):
        if random.random() < epsilon:
            arm = random.randint(0, n_arms - 1)
        else:
            arm = values.index(max(values))

        reward = simulate_reward(arm)
        total_reward += reward

        counts[arm] += 1
        # update mean
        values[arm] += (reward - values[arm]) / counts[arm]

    return total_reward / T


# -----------------------------
# 2. UCB
# -----------------------------
def ucb():
    counts = [0] * n_arms
    values = [0.0] * n_arms
    total_reward = 0

    for t in range(T):
        if t < n_arms:
            arm = t
        else:
            ucb_values = []
            for i in range(n_arms):
                bonus = math.sqrt((2 * math.log(t + 1)) / (counts[i]))
                ucb_values.append(values[i] + bonus)

            arm = ucb_values.index(max(ucb_values))

        reward = simulate_reward(arm)
        total_reward += reward

        counts[arm] += 1
        values[arm] += (reward - values[arm]) / counts[arm]

    return total_reward / T


# -----------------------------
# 3. Thompson Sampling
# -----------------------------
def thompson_sampling():
    successes = [1] * n_arms
    failures = [1] * n_arms
    total_reward = 0

    for t in range(T):
        samples = []
        for i in range(n_arms):
            samples.append(random.betavariate(successes[i], failures[i]))

        arm = samples.index(max(samples))

        reward = simulate_reward(arm)
        total_reward += reward

        if reward == 1:
            successes[arm] += 1
        else:
            failures[arm] += 1

    return total_reward / T


# Run all algorithms
random.seed(42)

eps_ctr = epsilon_greedy(0.1)
ucb_ctr = ucb()
ts_ctr = thompson_sampling()

# Results
print("Final Click-Through Rates (CTR):")
print("Epsilon-Greedy:", round(eps_ctr, 4))
print("UCB:", round(ucb_ctr, 4))
print("Thompson Sampling:", round(ts_ctr, 4))
