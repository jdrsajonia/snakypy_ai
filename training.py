import os
from stable_baselines3 import DQN
from stable_baselines3.common.callbacks import CheckpointCallback
from stable_baselines3.common.vec_env import DummyVecEnv

from objects.snakeEnv import SnakeEnv


DEVICE="cpu"
TOTAL_TIMESTEPS=5000000
# ============
# ENTRENAMIENTO
# ============
env = DummyVecEnv([lambda: SnakeEnv()])

# Carpeta donde se guardarán los checkpoints
checkpoint_dir = "./checkpoints_snake/"
os.makedirs(checkpoint_dir, exist_ok=True)

# Callback para guardar cada 100k timesteps
checkpoint_callback = CheckpointCallback(
    save_freq=100000,  
    save_path=checkpoint_dir,
    name_prefix="snake_dqn"
)

# Si ya existe un modelo, cargarlo; si no, crear uno nuevo
model_path = os.path.join(checkpoint_dir, "snake_dqn_latest.zip")
if os.path.exists(model_path):
    print("Cargando modelo entrenado...")
    model = DQN.load(model_path, env=env)
else:
    print("Creando modelo nuevo...")
    model = DQN("MlpPolicy", env, verbose=1, device=DEVICE)

# ENTRENAR
model.learn(
    total_timesteps=TOTAL_TIMESTEPS,  
    callback=checkpoint_callback
)


model.save(model_path)
print("Entrenamiento terminado y modelo guardado.")