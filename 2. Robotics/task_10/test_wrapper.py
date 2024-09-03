from stable_baselines3.common.env_checker import check_env
from ot2_gym_wrapper import OT2Env

# instantiate your custom environment
env = OT2Env(1, False) 
state = env.reset()
check_env(env, warn=True)
# Testing
# Number of episodes
num_episodes = 10
max_steps = 100

for episode in range(num_episodes):
    obs = env.reset()
    done = False
    step = 0

    while step < max_steps:
        # Take a random action from the environment's action space
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)

        print(f"Episode: {episode + 1}, Step: {step + 1}, Action: {action}, Reward: {reward}")
        step+=1
