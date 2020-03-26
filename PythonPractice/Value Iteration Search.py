import vi_util
import numpy as np
import copy

def main():
    S = np.array(
        [State(1, 1), State(1, 2), State(1, 3), State(2, 1), State(2, 3), State(3, 1), State(3, 2), State(3, 3),
         State(4, 1), State(4, 2), State(4, 3)])
    A = np.array(["u", "r", "d", "l"])
    P = vi_util.P
    term_index = [10, 6]
    i_obs = [5]
    i_count = 1

    # test_pairs key: [discount, reward]
    test_pairs = [[1.0, -0.04], [1.0, -0.25], [1.0, -0.01], [0.5, -0.04], [0.5, -0.25], [0.5, -0.01]]

    for discount, reward in test_pairs:
        U = valueIteration(S, A, P, reward, discount, term_index)
        print("Test Group", i_count, '\n' + "Discount: ", discount, '\n' + "Reward: ", reward, '\n')
        print("Utility Values:")
        print(U)
        policy = vi_util.getPolicyForGrid(S, U, A, P, term_index)
        vi_util.printPolicyForGrid(policy, 4, 3, i_obs)
        print('\n' + '-'*80 + '\n')
        i_count += 1


def valueIteration(S, A, P, reward, discount, term_index):
    U_prime = np.zeros(11)
    U_prime[term_index[0]] = 1
    U_prime[term_index[1]] = -1
    U = np.zeros(11)
    error = 0.01
    action_dict = {'u': 0, 'r': 1, 'd': 2, 'l': 3}
    while True:
        U = copy.deepcopy(U_prime)
        delta = 0
        for i, s in enumerate(S):
            if i in term_index:
                continue
            probs = []
            for a in A:
                # prob = 0
                # for j, p in enumerate(P[action_dict[a]][i]):
                #    prob += p * U[j]
                probs.append(getExpectedUtililty(a, s, S, U, P))
            U_max = max(probs)
            U_prime[i] = reward + discount * U_max
            if abs(U_prime[i] - U[i]) > delta:
                delta = abs(U_prime[i] - U[i])
        if delta < error * (1 - discount)/discount or delta == 0:
            break
    return U

def getExpectedUtililty(action, state, S, U, P):
    action_dict = {'u': 0, 'r': 1, 'd': 2, 'l': 3}
    prob = 0
    for j, p in enumerate(P[action_dict[action]][vi_util.getIndexOfState(S, state.x, state.y)]):
        prob += p * U[j]
    return prob

class State():
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    main()