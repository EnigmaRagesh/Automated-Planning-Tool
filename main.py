#!/usr/bin/env python3
import sys
import pprint
from parser import Action
from parser import PDDL_Parser
from planner import Astar_planner
from Astar import Astar

if __name__ == "__main__":
    # problem = "./PDDL/problem1.pddl"   #contains init and goal states
    # domain = "./PDDL/domain_1.pddl"       #contains problme description
    domain = "./PDDL/domain_2.pddl"   #contains init and goal states
    problem = "./PDDL/problem2.pddl"       #contains problme description
    parser = PDDL_Parser()
    print('PARSING\n')
    print('----------------------------')
    pprint.pprint(parser.scan_tokens(domain))
    print('----------------------------')
    pprint.pprint(parser.scan_tokens(problem))
    print('----------------------------')
    parser.parse_domain(domain)
    parser.parse_problem(problem)

    print('\n\n')
    print('Domain name:' + parser.domain_name)
    for act in parser.actions:
        print(act)
    print('----------------------------')
    print('Problem name: ' + parser.problem_name)
    print('Objects: ' + str(parser.objects))
    print('State: ' + str(parser.state))
    print('Positive goals: ' + str(parser.positive_goals))
    print('Negative goals: ' + str(parser.negative_goals))

 ## Planner
    planner = Astar_planner()
    plan = planner.solve(domain, problem)
    if plan:
        print('plan:')
        for act in plan:
            print(act)
    else:
        print('No plan was found')
    # Astar()