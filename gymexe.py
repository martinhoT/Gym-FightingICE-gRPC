import gym
import gym_fightingice
import random

env = gym.make("FightingiceDataNoFrameskip-v0", java_env_path="",port=4242, freq_restart_java=3)

obs = env.reset()
while True:
	obs = env.reset()
	done = False
	while not done:
		new_obs, reward, done, _ = env.step(random.randint(0, 55))


print("finish")