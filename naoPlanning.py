import random
from search import Problem
#from utils import from_state_to_dict, entropy


class NaoProblem(Problem):

    def __init__(self, initial, goal, intermediatePos, solution):
        # Here we define the goal state and we initialize the problem
        Problem.__init__(initial, goal)  # richiama il costruttore della classe padre
        self.intermediatePos = intermediatePos
        self.solution = solution


    def checkMove(self, state, next_move_name, next_move):  #  next_move is the list which contains preconditions, postconditions, duration
        # Here we exclude some moves from the available ones.

        state_dict = dict()
        for a in state:
            len_a = len(a)
            if len_a < 2:
                continue
            key = a[0]
            if len_a > 2:
                value = a[1:]
            else:
                value = a[1]
            if key not in state_dict:
                state_dict[key] = value



        #  Check if there is enough time to complete the next_move
        if state[1][2] < next_move[2]:  #  move[2] is the duration of the next_move
            return False

        # Check if the preconditions of the next_move are respected in the current state
        if 'standing' in next_move[0]:
            if state_dict['standing'] != move.preconditions['standing']:
                # If a 'standing' precondition is set, ensure that it's satisfied
                return False

        # Criterion 3: is the move different from the one which was performed last?
        last_move = state_dict['choreography'][-1]
        if move_name == last_move:
            return False

        # If no criterion was matched, we accept the move
        return True

    def actions(self, state):
        # Return the actions that can be executed in the given state.
        accepted_actions = []
        for move_name, move in self.intermediatePos.items():
            if self.checkMove(state, move_name, move):
                accepted_actions.append(move_name)
        random.shuffle(accepted_actions)
        return accepted_actions

    def result(self, state, action):
        # Given state and action, return a new state that is the result of the action.
        # Action is assumed to be a valid action in the state
        nao_move = self.available_moves[action]
        state_dict = from_state_to_dict(state)

        # Here we compute the new 'entropy' value
        full_choreography = [*self.previous_moves_done, *state_dict['choreography'], action]
        new_entropy = entropy(full_choreography)

        # Here we compute the new 'standing' value
        if 'standing' in nao_move.postconditions:
            # Apply the postconditions of this move
            new_standing = nao_move.postconditions['standing']
        else:
            # This move doesn't affect the 'standing' value
            new_standing = state_dict['standing']

        return (('choreography', (*state_dict['choreography'], action)),
                ('standing', new_standing),
                ('remaining_time', state_dict['remaining_time'] - nao_move.duration),
                ('moves_done', state_dict['moves_done'] + 1),
                ('entropy', new_entropy))

    def goal_test(self, state):
        # Given a state, return True if state is a goal state or False, otherwise
        state_dict = from_state_to_dict(state)
        goal_dict = from_state_to_dict(self.goal)

        goal_remaining_time = goal_dict['remaining_time']
        a = goal_remaining_time
        b = goal_remaining_time + self.time_threshold

        # Here we test all the existing constraints
        time_constraint = (a <= state_dict['remaining_time'] <= b)
        moves_done_constraint = (state_dict['moves_done'] >= goal_dict['moves_done'])
        entropy_constraint = (state_dict['entropy'] >= goal_dict['entropy'])
        standing_constraint = (state_dict['standing'] == goal_dict['standing'])

        if goal_dict['standing'] is None:
            # No standing precondition was explicitly stated: then,
            # we can safely ignore the standing_constraint
            return time_constraint and moves_done_constraint and entropy_constraint
        else:
            # In this case we must consider also the standing_constraint
            return time_constraint and moves_done_constraint and entropy_constraint and standing_constraint