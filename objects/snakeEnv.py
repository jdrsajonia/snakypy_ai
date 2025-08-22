# objects/snakeEnv.py
import gymnasium as gym
from gymnasium import spaces
import numpy as np

from objects.entities import spaceObject, snakeObject

class SnakeEnv(gym.Env):
    metadata = {"render_modes": []}

    def __init__(self, dimension=(15, 30)):
        super().__init__()

        self.dimension = dimension
        self.snake = snakeObject(dimension)
        self.space = spaceObject(dimension)
        self.space.put_apple(4)

        # Acción discreta: 0=up, 1=left, 2=down, 3=right
        self.action_space = spaces.Discrete(4)

        # Observación normalizada [0,1]
        self.observation_space = spaces.Box(
            low=0.0, high=1.0,
            shape=(6,), dtype=np.float32
        )

        self.score = 0

    def reset(self, *, seed=None, options=None):
        super().reset(seed=seed)
        self.snake = snakeObject(self.dimension)
        self.space = spaceObject(self.dimension)
        self.space.put_apple(4)
        self.score = 0
        obs = self._get_state()
        return obs, {}  # obs, info

    def step(self, action):
        directions = ["w", "a", "s", "d"]
        action_str = directions[action]

        old_head = self.snake.get_head_position()
        apple = list(self.space.apples_coordinates)[0]
        old_dist = np.linalg.norm(np.array(old_head) - np.array(apple))

        should_grow = self.space.detect_apple(self.snake, action_str)
        self.snake.move_to(action_str, should_grow)

        reward = -0.05

        if should_grow:
            reward += 10
            self.score += 1

        terminated = False
        truncated = False

        if self.snake.collision:
            terminated = True
            reward -= 50

        new_head = self.snake.get_head_position()
        apple = list(self.space.apples_coordinates)[0]
        new_dist = np.linalg.norm(np.array(new_head) - np.array(apple))

        if new_dist < old_dist:
            reward += 0.2
        else:
            reward -= 0.2

        return self._get_state(), reward, terminated, truncated, {}

    def _get_state(self):
        head_x, head_y = self.snake.get_head_position()
        apple_x, apple_y = list(self.space.apples_coordinates)[0]

        direction_map = {
            (0, -1): "w", (-1, 0): "a", (0, 1): "s", (1, 0): "d",
            "w": "w", "a": "a", "s": "s", "d": "d"
        }
        dir_value = self.snake.current_direction
        dir_str = direction_map.get(dir_value, "w")
        direction = ["w", "a", "s", "d"].index(dir_str)

        max_x, max_y = self.dimension
        norm = lambda v, m: v / m

        return np.array([
            norm(head_x, max_x),
            norm(head_y, max_y),
            norm(apple_x, max_x),
            norm(apple_y, max_y),
            min(self.score / 50.0, 1.0),
            direction / 3.0
        ], dtype=np.float32)
