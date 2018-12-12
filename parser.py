
import sys
import Pddlpy
from  pddlpy import DomainProblem

def main():
    domainfile = "../PDDL/Operators.pddl" 
    problemfile = "../PDDL/initial_goal_1.pddl"
    domprob = DomainProblem(domainfile, problemfile)
    print()
    print("DOMAIN PROBLEM")
    print("objects")
    print("\t", domprob.worldobjects())
    print("operators")
    print("\t", list( domprob.operators() ))
    print("init",)
    print("\t", domprob.initialstate())
    print("goal",)
    print("\t", domprob.goals())

    # print()
    # ops_to_test = { 1:"op2", 2:"move", 3:"move", 4:"move", 5:"A1" }
    # op = ops_to_test[demonumber]
    # print("ground for operator", op, "applicable if (adjacent loc1 loc2)")
    # for o in domprob.ground_operator(op):
    #     if ("adjacent","loc1","loc2") in o.precondition_pos:
    #         print()
    #         print( "\tvars", o.variable_list )
    #         print( "\tpre+", o.precondition_pos )
    #         print( "\tpre-", o.precondition_neg )
    #         print( "\teff+", o.effect_pos )
    #         print( "\teff-", o.effect_neg )


if __name__ == '__main__':
    main()