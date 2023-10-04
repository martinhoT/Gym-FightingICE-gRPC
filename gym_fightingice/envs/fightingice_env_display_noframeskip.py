import random

from gymnasium import spaces

from gym_fightingice.envs.fightingice_env_base import FightingiceEnv_Base
from gym_fightingice.envs.gym_ai_display import GymAIDisplay
from gym_fightingice.envs.Machete import Machete


class FightingiceEnv_Display_NoFrameskip(FightingiceEnv_Base):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.observation_space = spaces.Box(low=0, high=1, shape=(96, 64, 1))

    def _start_gateway(self, p2=Machete):
        super()._start_gateway(p2, ai_class=GymAIDisplay, ai_class_kwargs={"frameskip": False})


if __name__ == "__main__":
    env = FightingiceEnv_Display_NoFrameskip()

    while True:
        obs = env.reset()
        done = False

        while not done:
            new_obs, reward, done, _ = env.step(random.randint(0, 10))

    print("finish")
