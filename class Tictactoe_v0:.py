class Tictactoe_v0:
    def __init__(self):
        self.board = [0] * 9
        self.wining_position = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                                [0, 4, 8], [6, 4, 2]]
        self.current_turn = 1
        self.player_mark = 1

    def reset(self, is_human_first):
        self.board = [0] * 9
        self.current_turn = 1
        self.player_mark = 1 if is_human_first else -1
        if not is_human_first:
            self.env_act()
        return self.board.copy()

    def check_win(self):
        for pst in self.wining_position:
            if str(self.board[pst[0]]) + str(self.board[pst[1]]) + str(self.board[pst[2]]) in ['111', '-1-1-1']:
                if self.current_turn == self.player_mark:
                    return 1, True
                return -1, True
        if 0 not in self.board:
            return 0, True
        return 0, False

    def env_act(self):
        action = random.choice([i for i in range(len(self.board)) if self.board[i] == 0])
        for pst in self.wining_position:
            com = str(self.board[pst[0]]) + str(self.board[pst[1]]) + str(self.board[pst[2]])
            if com.replace('0', '') == str(self.current_turn) * 2:
                if self.board[pst[0]] == 0:
                    action = pst[0]
                elif self.board[pst[1]] == 0:
                    action = pst[1]
                else:
                    action = pst[2]
        if self.board[action] != 0:
            raise Exception('Invalid action')
        self.board[action] = self.current_turn
        reward, done = self.check_win()
        self.current_turn = self.current_turn * -1
        return reward, done

    def step(self, action):
        if self.board[action] != 0:
            raise Exception('Invalid action')
        self.board[action] = self.current_turn
        reward, done = self.check_win()
        self.current_turn = self.current_turn * -1
        if done:
            return self.board.copy(), reward, done, None
        reward, done = self.env_act()
        return self.board.copy(), reward, done, None
        class EpsilonGreedy:
    def __init__(self, epsilon):
        self.epsilon = epsilon

    def perform(self, q_value, action_space: list = None):
        prob = np.random.sample()  # get probability of taking random action
        if prob <= self.epsilon:  # take random action
            if action_space is None:  # all action are available
                return np.random.randint(len(q_value))
            return np.random.choice(action_space)
        else:  # take greedy action
            if action_space is None:
                return np.argmax(q_value)
            return max([[q_value[a], a] for a in action_space], key=lambda x: x[0])[1]

    def decay(self, decay_value, lower_bound):
    
        self.epsilon = max(self.epsilon * decay_value, lower_bound)
        class ExperienceReplay:
    def  __init__(self, e_max: int):
        if e_max <= 0:
            raise ValueError('Invalid value for memory size')
        self.e_max = e_max
        self.memory = list()
        self.index = 0

    def add_experience(self, sample: list):
        if len(sample) != 5:
            raise Exception('Invalid sample')
        if len(self.memory) < self.e_max:
            self.memory.append(sample)
        else:
            self.memory[self.index] = sample
        self.index = (self.index + 1) % self.e_max

    def sample_experience(self, sample_size: int, cer_mode: bool):
        samples = random.sample(self.memory, sample_size)
        if cer_mode:
            samples[-1] = self.memory[self.index - 1]
        # state_samples, action_samples, reward_samples, next_state_samples, done_samples
        s_batch, a_batch, r_batch, ns_batch, done_batch = map(np.array, zip(*samples))
        return s_batch, a_batch, r_batch, ns_batch, done_batch

    def get_size(self):
        return len(self.memory)
        class DQN(BaseModel):
    def __init__(self, discount_factor: float, epsilon: float, e_min: int, e_max: int):
        super().__init__(discount_factor, epsilon, e_min, e_max)
        self.gamma = discount_factor
        self.epsilon_greedy = EpsilonGreedy(epsilon)
        self.e_min = e_min
        self.exp_replay = ExperienceReplay(e_max)
        self.training_network = Sequential()
        self.target_network = Sequential()
        self.cache = list()

    def observe(self, state, action_space: list = None):
        q_value = self.training_network.predict(np.array([state])).ravel()
        if action_space is not None:
            return max([[q_value[a], a] for a in action_space], key=lambda x: x[0])[1]
        return np.argmax(q_value)

    def observe_on_training(self, state, action_space: list = None) -> int:
        q_value = self.training_network.predict(np.array([state])).ravel()
        action = self.epsilon_greedy.perform(q_value, action_space)
        self.cache.extend([state, action])
        return action

    def take_reward(self, reward, next_state, done):
        self.cache.extend([reward, next_state, done])
        self.exp_replay.add_experience(self.cache.copy())
        self.cache.clear()

    def train_network(self, sample_size: int, batch_size: int, epochs: int, verbose: int = 2, cer_mode: bool = False):
        if self.exp_replay.get_size() >= self.e_min:
            # state_samples, action_samples, reward_samples, next_state_samples, done_samples
            s_batch, a_batch, r_batch, ns_batch, done_batch = self.exp_replay.sample_experience(sample_size, cer_mode)
            states, q_values = self.replay(s_batch, a_batch, r_batch, ns_batch, done_batch)
            history = self.training_network.fit(states, q_values, epochs=epochs, batch_size=batch_size, verbose=verbose)
            return history.history['loss']

    def replay(self, states, actions, rewards, next_states, terminals):
        q_values = self.target_network.predict(np.array(states))  # get q value at state t by target network
        nq_values = self.target_network.predict(np.array(next_states))  # get q value at state t+1 by target network
        for i in range(len(states)):
            a = actions[i]
            done = terminals[i]
            r = rewards[i]
            if done:
                q_values[i][a] = r
            else:
                q_values[i][a] = r + self.gamma * np.max(nq_values[i])
        return states, q_values

    def update_target_network(self):
        self.target_network.set_weights(self.training_network.get_weights())
        env = Tictactoe_v0()
agent = DQN(0.7, 1, 4096, 1048576)
op1 = optimizers.RMSprop(learning_rate=0.00025)
agent.training_network.add(Dense(128, activation='relu', input_shape=(9,)))
agent.training_network.add(Dense(128, activation='relu'))
agent.training_network.add(Dense(9, activation='linear'))
agent.training_network.compile(optimizer=op1, loss=losses.mean_squared_error)


op2 = optimizers.RMSprop(learning_rate=0.00025)
agent.target_network.add(Dense(128, activation='relu', input_shape=(9,)))
agent.target_network.add(Dense(128, activation='relu'))
agent.target_network.add(Dense(9, activation='linear'))
agent.target_network.compile(optimizer=op2, loss=losses.mean_squared_error)
agent.update_target_network()
