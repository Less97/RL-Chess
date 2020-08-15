import gym
import gym_chess
import random
gym.envs.registry.all()
env = gym.make('Chess-v0')
state = env.reset()

done = False
r = 0
episodes = 10000
currentEpisode = 0
while currentEpisode<episodes:
    print('episode:'+str(currentEpisode))
    while not done:
        action = random.choice(env.legal_moves)
        observation,reward,done,_ = env.step(action)
        r+=reward
    env.reset()
    done = False
    currentEpisode+=1
    print('total reward:'+str(r))
    r=0

