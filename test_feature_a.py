import pytest
from feature_a import feature_a
from unittest.mock import patch
from io import StringIO
from tabulate import tabulate

class TestFeatureA:
    ''' This class contains the test cases for feature A '''
    def setup_method(self):
        ''' This method sets up the required objects for testing '''
        self.ins_a = feature_a()
        self.sprint_points = [5, 8, 10, 12]
        self.average_velocity = 8.75

    def test_input(self):
        ''' This method tests the input method of feature A '''
        with patch('builtins.input', side_effect=[4, 5, 8, 10, 12]):
            assert self.ins_a.input() == self.sprint_points
            print(self.sprint_points)

    def test_calculate_velocity(self):
        ''' This method tests the calculate_velocity method of feature A '''
        assert self.ins_a.calculate_velocity(self.sprint_points) == self.average_velocity
        print(self.average_velocity)

    def test_empty_input(self):
        ''' This method tests the input method of feature A with no sprint points '''
        with patch('builtins.input', side_effect=[0]):
            assert self.ins_a.input() == []
            print([])

    def test_empty_calculate_velocity(self):
        ''' This method tests the calculate_velocity method of feature A with no sprint points '''
        assert self.ins_a.calculate_velocity([]) == 0
        print(0)