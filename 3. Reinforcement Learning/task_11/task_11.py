import wandb
from stable_baselines3 import PPO
from ot2_gym_wrapper import OT2Env
from stable_baselines3.common.evaluation import evaluate_policy
from wandb.integration.sb3 import WandbCallback
from datetime import datetime

env = OT2Env(False)

now = datetime.now()
date_time = now.strftime("%Y-%m-%d.%H:%M:%S")
experiment_name = 'K_F_' + date_time

config = {
    "model": "PPO",
    "policy_type": "MlpPolicy",
    "n_steps": 1024,
    "batch_size": 32,
    "total_timesteps": 10_000_000,
    "gamma": 0.99,
    "lr": 0.0001
}

run = wandb.init(
    project="task_11",
    name=experiment_name,
    config=config,
    sync_tensorboard=True  
)

model = PPO(config['policy_type'],
            env,
            verbose=1,
            gamma=config['gamma'],
            learning_rate=config['lr'],
            n_steps=config['n_steps'],
            batch_size=config['batch_size'],
            tensorboard_log=f"runs/{run.id}")


wandb_callback = WandbCallback(model_save_freq=10000,
                               model_save_path=f"models/{run.id}",
                               verbose=2)


for i in range(100):
    model.learn(
        total_timesteps=100_000,
        callback=wandb_callback,
        progress_bar=True,
        reset_num_timesteps=True
    )
    model.save(f'model{i}') 


# Evaluate the trained model
mean_reward, _ = evaluate_policy(model, env, n_eval_episodes=10, deterministic=True)
wandb.log({"mean_reward": mean_reward})

# Finish the WandB run
run.finish()
