
import Queue
import time
import math

class Plus_uno():
    def __init__(self, goal):
        self.goal = goal

    def get_start_state(self):
        return (0,) + (1,) * 8

    def is_goal_state(self, state):
        return state == (self.goal,) * 9

    def get_successors(self, state):
        state = list(state)
        values = list(set(state))
        values.sort()

        successors = []

        for val in values:
            for val2 in values:
                new_suc = self.gen_successor(state, (val, val2))
                if new_suc:
                    successors.append(new_suc)
                new_suc = self.gen_successor(state, (val2, val))
                if new_suc:
                    successors.append(new_suc)
        return successors

    # helper method
    def gen_successor(self, tiles, move):
        if sum(move) > self.goal:
            return

        new_state = tiles[:]

        try:
            new_state.remove(move[0])
            new_state.remove(move[1])

            new_val = move[0] + 1
            new_val2 = move[0] + move[1]

            new_state.append(new_val)
            new_state.append(new_val2)
            new_state.sort()

            return tuple(new_state), [move]
        except:
            return

    def get_cost_of_actions(self, actions):
        return len(actions)

    def good_actions(self, actions):
        if len(actions) > 4 and actions[-4:] != [(self.goal-1, 1)] * 4:
            return False
        return True

class Plus_uno2():
    def __init__(self, goal):
        self.goal = goal

    def get_start_state(self):
        return (0,) + (1,) * 4

    def is_goal_state(self, state):
        return state == (self.goal-1,) * 4 + (self.goal,)

    def get_successors(self, state):
        state = list(state)
        values = list(set(state))
        values.sort()

        successors = []
        states = set()

        for val in values:
            for val2 in values:
                new_suc = self.gen_successor(state, (val, val2))
                if new_suc:
                    successors.append(new_suc)
                new_suc = self.gen_successor(state, (val2, val))
                if new_suc:
                    successors.append(new_suc)
        return successors

    # helper method
    def gen_successor(self, tiles, move):
        if sum(move) > self.goal:
            return

        new_state = tiles[:]

        try:
            new_state.remove(move[0])
            new_state.remove(move[1])

            new_val = move[0] + 1
            new_val2 = move[0] + move[1]

            new_state.append(new_val)
            new_state.append(new_val2)
            new_state.sort()

            return tuple(new_state), [move]
        except:
            return

    def get_cost_of_actions(self, actions):
        return len(actions)

    def good_actions(self, actions):
        if len(actions) > 4 and actions[-4:] != [(self.goal-1, 1)] * 4:
            return False
        return True


def null_heuristic(state, problem=None):
    return 0

# number of things not satisfying goal state / 2
def f_heuristic(state, problem):
    not_matching = len(filter(lambda x: x != problem.goal, state))

    return not_matching / 2


# stuff returned in (state, path) pairs
def aStarSearch(problem, heuristic=null_heuristic):
    closed = set([problem.get_start_state()])
    fringe = Queue.PriorityQueue()
    for successor in problem.get_successors(problem.get_start_state()):
        state, path = successor
        cost = problem.get_cost_of_actions(path) + heuristic(state, problem)
        to_put = (cost, (state, path))
        fringe.put(to_put)

    while not fringe.empty():
        _, (state, path) = fringe.get()
        if problem.is_goal_state(state):
            print 'states checked: {}'.format(len(closed))
            return path

        if state not in closed:
            closed.add(state)
            for successor in problem.get_successors(state):
                new_state, new_path = successor
                if new_state in closed:
                    continue

                new_path = path + new_path
                cost = problem.get_cost_of_actions(new_path) + heuristic(new_state, problem)
                to_put = (cost, (new_state, new_path))
                fringe.put(to_put)

    raise Exception('Error: path not found')


def main():
    for i in range(2,21):
        print '-' * 40
        print 'goal: {}'.format(i)
        problem = Plus_uno2(i)
        path = aStarSearch(problem, heuristic=f_heuristic)
        path += [(i-1, 1)] * 4
        print 'path: {}'.format(path)


if __name__ == '__main__':
    main()
