import pytest
from feature_b import FeatureB
from unittest.mock import patch
from io import StringIO
from tabulate import tabulate

class TestFeatureB:
    ''' This class contains the test cases for feature B '''
    def setup_method(self):
        ''' This method sets up the required objects for testing '''
        self.ins_b = FeatureB()
        self.team_members_details = [{'name': 'John', 'days_off': 2, 'days_for_scrum_commitment': 3, 'min_hours_per_day': 6, 'max_hours_per_day': 8}, {'name': 'Doe', 'days_off': 3, 'days_for_scrum_commitment': 2, 'min_hours_per_day': 7, 'max_hours_per_day': 9}]
        self.team_min_cap = 65
        self.team_max_cap = 85

    def test_input_team_members_details(self):
        ''' This method tests the input_team_members_details method of feature B '''
        with patch('builtins.input', side_effect=['John', 2, 3, '6-8', 'Doe', 3, 2, '7-9']):
            assert self.ins_b.input_team_members_details(2) == self.team_members_details
            print(self.team_members_details)

    def test_calculate_available_hours(self):
        ''' This method tests the calculate_available_hours method of feature B '''
        sprint_days = 10
        assert self.ins_b.calculate_available_hours(sprint_days, self.team_members_details) == (self.team_members_details, self.team_min_cap, self.team_max_cap)
        print(self.team_members_details, self.team_min_cap, self.team_max_cap)

    def test_empty_input_team_members_details(self):
        ''' This method tests the input_team_members_details method of feature B with no team members '''
        with patch('builtins.input', side_effect=[]):
            assert self.ins_b.input_team_members_details(0) == []
            print([])

    def test_empty_calculate_available_hours(self):
        ''' This method tests the calculate_available_hours method of feature B with no team members '''
        sprint_days = 0
        assert self.ins_b.calculate_available_hours(sprint_days, []) == ([], 0, 0)
        print([], 0, 0)
