import gym
import numpy as np

env = gym.make('FrozenLake-v1', is_slippery=True)  # Default is_slippery=True

Q = np.zeros([env.observation_space.n, env.action_space.n])

learning_rate = 0.8
discount = 0.95
num_episodes = 2000

rewards = []

for i in range(num_episodes):
    state, _ = env.reset()
    done = False
    total_rewards = 0

    while not done:
        action = np.argmax(Q[state, :] + np.random.randn(1, env.action_space.n) * (1. / (i + 1)))

        new_state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated

        Q[state, action] = Q[state, action] + learning_rate * (reward + discount * np.max(Q[new_state, :]) - Q[state, action])

        total_rewards += reward
        state = new_state

    rewards.append(total_rewards)

    # 🔥 Add a print every 100 episodes
    if (i + 1) % 100 == 0:
        print(f"Episode {i+1}: Average Reward (last 100 episodes) = {np.mean(rewards[-100:]):.2f}")

# After training
print("\nTraining completed.")
print(f"Overall average reward: {np.mean(rewards):.2f}")

# Optional: Print final Q-Table
print("\nFinal Q-Table:")
print(Q)
