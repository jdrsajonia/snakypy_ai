from time import sleep
from objects.snakeEnv import SnakeEnv
from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv

env = DummyVecEnv([lambda: SnakeEnv()])

model = DQN.load("./checkpoints_snake/snake_dqn_latest.zip", env=env)
# model = DQN.load("./checkpoints_snake/snake_dqn_100000_steps.zip", env=env)
obs = env.reset()
done = False
clear = "\033[H\033[J"
snake_longs=[]

while not done:
    
    action, _ = model.predict(obs)
    obs, reward, done, _ = env.step(action)
    
    if done:
        break
    print(clear)
    print(env.envs[0].space.render_str_game(env.envs[0].snake))
    snake_longs.append(env.envs[0].snake.long)
    print("Reward:", reward, "Done:", done, "actual_long:", env.envs[0].snake.long, "maxlong:", max(snake_longs))

    
    sleep(0.1)
    
