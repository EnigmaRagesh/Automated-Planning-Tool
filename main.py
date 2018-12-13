#!/usr/bin/env python3

from planner import planner
from parser import parser
from Astar import Astar

if __name__ == "__main__":
    parser()
    planner()
    Astar()