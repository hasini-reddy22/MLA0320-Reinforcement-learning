import random
import math

# Parameters
EPISODES = 5000
STEPS = 20
ALPHA = 0.01  # learning rate
GAMMA = 0.9

# Policy parameter
theta = 0.0


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


# Simulated market return
def market_return():
    # Random return between -1 and +1
    return random.uniform(-1, 1)


# Sample action from policy
def choose_action(theta):
    prob = sigmoid(theta)
    if random.random() < prob:
        return 1  # invest
    return 0  # hold


# Compute gradient of log policy
def grad_log_policy(action, theta):
    prob = sigmoid(theta)
    if action == 1:
        return 1 - prob
    else:
        return -prob


# Training loop (REINFORCE)
def train():
    global theta

    for ep in range(EPISODES):
        episode = []

        # Generate episode
        for t in range(STEPS):
            action = choose_action(theta)
            r = market_return()

            reward = action * r  # only gain if invested
            episode.append((action, reward))

        # Compute returns and update policy
        G = 0
        for t in reversed(range(len(episode))):
            action, reward = episode[t]
            G = reward + GAMMA * G

            grad = grad_log_policy(action, theta)
            theta += ALPHA * G * grad

        # Optional: print progress
        if (ep + 1) % 1000 == 0:
            print(f"Episode {ep+1}, Theta: {round(theta, 4)}")


# Run training
random.seed(42)
train()

# Final policy
final_prob = sigmoid(theta)

print("\nFinal Policy:")
print("Probability of Investing:", round(final_prob, 4))
