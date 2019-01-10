import sys
import numpy as np
sys.path.append('../mover_library/')
from samplers import *
from utils import get_pick_domain, get_place_domain

from feasibility_checkers.pick_feasibility_checker import PickFeasibilityChecker
from feasibility_checkers.place_feasibility_checker import PlaceFeasibilityChecker


class Generator:
    def __init__(self, operator_name, problem_env):
        self.problem_env = problem_env
        self.env = problem_env.env
        if operator_name == 'two_arm_pick':
            self.domain = get_pick_domain()
            self.feasibility_checker = PickFeasibilityChecker(problem_env)
        elif operator_name == 'two_arm_place':
            if problem_env.name == 'convbelt':
                place_domain = get_place_domain(problem_env.regions['object_region'])
            else:
                place_domain = get_place_domain(problem_env.regions['entire_region'])

            self.domain = place_domain
            self.feasibility_checker = PlaceFeasibilityChecker(problem_env)

    def choose_next_point(self, node, n_iter):
        raise NotImplementedError

