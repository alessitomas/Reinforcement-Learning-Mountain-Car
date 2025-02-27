import gymnasium as gym

env = gym.make('MountainCar-v0')
(state,_) = env.reset()

# primeiro elemento é a posição do carro e o segundo é a velocidade do carro:
print('State space: ', env.observation_space)


# There are 3 discrete deterministic actions:
# 0: Accelerate to the left
# 1: Don’t accelerate
# 2: Accelerate to the right

print('Action space: ', env.action_space)


print(env.observation_space.low)
print(env.observation_space.high)
