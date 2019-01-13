#!/usr/bin/env python3

#  This is completely copied form the pyddl-master folder
from parser import PDDL_Parser
#   """
#     Implements A* search to find a plan for the given problem.
#     Arguments:
#     problem   - a pyddl Problem
#     heuristic - a heuristic to use (h(state) = 0 by default)
#     state0    - initial state (problem.initial_state by default)
#     goal      - tuple containing goal predicates and numerical conditions
#                 (default is (problem.goals, problem.num_goals))
#     monotone  - if True, only applies actions by ignoring delete lists
#     verbose   - if True, prints statistics before returning
#     """
def Astar_planner(problem, state0=None, goal=None,  heuristic=None,monotone=False, verbose=True):
           
     # Parser
    parser = PDDL_Parser()
    parser.parse_domain(domain)
    parser.parse_problem(problem)
    # Parsed data
    actions = parser.actions
    heuristic = null_heuristic
    state0 = parser.state
    goal = parser.positive_goals
    #   initial conditions
    states_explored = 0
    closed = set()
    pred = [(heuristic(state0), -state0.cost, state0)]
    heapq.heapify(pred)
    start = time()




    while True:
        if len(pred) == 0:
            if verbose: print('States Explored: %d' % states_explored)
            return None
        # Take s in nexts which minimises the f+h
        h, _, node = heapq.heappop(pred)
        states_explored += 1
        # Goal test
        if node.is_true(*goal):
            plan = node.plan()
            return plan
        # Expand node if we haven't seen it before
        if node not in closed:
            closed.add(node)
            # Apply all applicable actions to get nexts
            nexts = set(node.apply(action, monotone)
                             for action in problem.grounded_actions
                             if node.is_true(action.preconditions,
                                             action.num_preconditions))
            # Compute heuristic and add to pred
            for nex in nexts:
                if nex not in closed:
                    f = nex.cost + heuristic(nex)
                    heapq.heappush(pred, (f, -nex.cost, nex))

########## HEURISTICS ##########

def null_heuristic(state):
    """Admissible, but trivial heuristic"""
    return 0

def plan_cost(plan):
    """Convert a plan to a cost, handling nonexistent plans"""
    if plan is None:
        return float('inf')
    else:
        return len(plan)

