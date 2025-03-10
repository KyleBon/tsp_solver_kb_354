import unittest

from tsp_solver_kb_354.algorithms.Asearch import a_star_search
from tsp_solver_kb_354.algorithms.hill_climbing import hill_climbing
from tsp_solver_kb_354.algorithms.random_search import random_search
from tsp_solver_kb_354.algorithms.simulated_annealing import simulated_annealing
from tsp_solver_kb_354.utils import generate_random_cities


class TestTSPHillClimbing(unittest.TestCase):
    def setUp(self):
        self.cities = generate_random_cities(6)

    def test_hill_climbing(self):
        route, distance = hill_climbing(self.cities)
        self.assertIsInstance(route, list)
        self.assertIsInstance(distance, float)



if __name__ == "__main__":
    unittest.main()