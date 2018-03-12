#!/usr/bin/env python
"""Unittests for Carla Catkinization."""

import unittest
import rosunit

class TestCarlaCatkinization(unittest.TestCase):
    """ Carla Catkinization Test Case."""

    def test_python_module(self):
        """Tests if python module has been installed and can be loaded."""
        import pkgutil
        carla_loader = pkgutil.find_loader('carla')
        self.assertTrue(carla_loader is not None)

if __name__ == '__main__':
    rosunit.unitrun('carla_binary_catkin', 'test_carla_catkinization',
                    TestCarlaCatkinization)
