import ddz
import dqn

if __name__ == '__main__':
    env = ddz()
    RL = DeepQNetwork(env.n_actions,
                      env.n_features,
                      learning_rate=0.01,
                      reward_decay=0.9,
                      e_greedy=0.9,
                      replace_target_iter=200,
                      memory_size=2000,
                      # output_graph=True
                      )
