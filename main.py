#!/usr/bin/env python3
import sys
import pprint
from parser import Action
from parser import PDDL_Parser
from planner import Propositional_Planner
from Astar import Astar

if __name__ == "__main__":
    domain= "./PDDL/initial_goal_1.pddl"   #contains init and goal states
    problem = "./PDDL/Operators.pddl"       #contains problme description
    parser = PDDL_Parser()
    print('----------------------------')
    pprint.pprint(parser.scan_tokens(domain))
    print('----------------------------')
    pprint.pprint(parser.scan_tokens(problem))
    print('----------------------------')
    parser.parse_domain(domain)
    parser.parse_problem(problem)
    print('Domain name:' + parser.domain_name)
    for act in parser.actions:
        print(act)
    print('----------------------------')
    print('Problem name: ' + parser.problem_name)
    print('Objects: ' + str(parser.objects))
    print('State: ' + str(parser.state))
    print('Positive goals: ' + str(parser.positive_goals))
    print('Negative goals: ' + str(parser.negative_goals))

    # planner()
    planner = Propositional_Planner()
    plan = planner.solve(domain, problem)
    if plan:
        print('plan:')
        for act in plan:
            print(act)
    else:
        print('No plan was found')
    # Astar()