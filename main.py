#!/usr/bin/env python3
import sys
import pprint
from parser import Action
from parser import PDDL_Parser
from planner import Astar_planner
from Astar import Astar

if __name__ == "__main__":
    '''
    PDDL to list
    '''
    # problem = "./PDDL/problem1.pddl"   #contains init and goal states
    # domain = "./PDDL/domain_1.pddl"       #contains problme description
    domain = "./PDDL/domain_2.pddl"   #contains init and goal states
    problem = "./PDDL/problem2.pddl"       #contains problme description
    parser = PDDL_Parser()

    '''
    PDDL grounded form
    '''
    parser.parse_domain(domain)
    parser.parse_problem(problem)
    print('\n\n')
    print('Domain name:' + parser.domain_name)
    print('\n')
    for act in parser.actions:
        print(act)
    print('----------------------------')
    print('\nProblem name: ' + parser.problem_name)
    print('\nObjects: ' + str(parser.objects))
    print('\nState: ' + str(parser.state))
    print('\nPositive goals: ' + str(parser.positive_goals))
    print('\nNegative goals: ' + str(parser.negative_goals))
    