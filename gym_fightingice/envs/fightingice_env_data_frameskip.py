import random

from gymnasium import spaces

from gym_fightingice.envs.fightingice_env_base import FightingiceEnv_Base
from gym_fightingice.envs.gym_ai import GymAI
from gym_fightingice.envs.Machete import Machete


class FightingiceEnv_Data_Frameskip(FightingiceEnv_Base):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.observation_space = spaces.Box(low=0, high=1, shape=(143,))

    def _start_gateway(self, p2=Machete):
        super()._start_gateway(p2, ai_class=GymAI, ai_class_kwargs={"frameskip": True})


if __name__ == "__main__":
    env = FightingiceEnv_Data_Frameskip()

    while True:
        obs = env.reset()
        done = False

        while not done:
            new_obs, reward, done, _ = env.step(random.randint(0, 10))

    print("finish")
