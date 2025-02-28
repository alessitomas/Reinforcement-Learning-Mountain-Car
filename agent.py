import numpy as np

def __init__(self, env, alpha, gamma, epsilon, epsilon_min, epsilon_dec, episodes):

    self.env = env

    # discretizando o espaco de estados
    self.num_states = (env.observation_space.high - env.observation_space.low)*np.array([10, 100])
    self.num_states = np.round(self.num_states, 0).astype(int) + 1

    #inicializando uma q-table com 3 dimensoes: x, velocidade, acao
    self.Q = np.zeros([self.num_states[0], self.num_states[1], env.action_space.n])


def select_action(self, state_adj):
    if np.random.random() < 1 - self.epsilon:
        return np.argmax(self.Q[state_adj[0], state_adj[1]]) 
    return np.random.randint(0, self.env.action_space.n)


def transform_state(self, state):
    state_adj = (state - self.env.observation_space.low)*np.array([10, 100])
    return np.round(state_adj, 0).astype(int)


(state,_) = self.env.reset()
state_adj = self.transform_state(state)


action = self.select_action(state_adj)
next_state, reward, done, truncated, _ = self.env.step(action) 
next_state_adj = self.transform_state(next_state)