import pytest
import mock

from feature_b import FeatureB

class TestFeatureA:
    
    def test_input_sprint_days(self):
        instance = FeatureB()
        mock_input = mock.Mock()
        mock_input.side_effect = [10]
        with mock.patch('builtins.input', mock_input):
            assert instance.input_sprint_days() == 10

    def test_input_no_team_members(self):
        instance = FeatureB()
        mock_input = mock.Mock()
        mock_input.side_effect = [3]
        with mock.patch('builtins.input', mock_input):
            assert instance.input_no_team_members() == 3

    def test_input_team_members_details(self):
        instance = FeatureB()
        mock_input = mock.Mock()
        
        mock_input.side_effect = [
            'Alice', 2, 2, "8-10",
            'Bob', 1, 2, "4-7",
            'John', 4, 3, "5-8"
        ]
        with mock.patch('builtins.input', mock_input):
            assert instance.input_team_members_details(3) == [
                {'name': 'Alice', 'days_off': 2, 'days_for_scrum_commitment': 2, 'min_hours_per_day': 8, 'max_hours_per_day': 10},
                {'name': 'Bob', 'days_off': 1, 'days_for_scrum_commitment': 2, 'min_hours_per_day': 4, 'max_hours_per_day': 7},
                {'name': 'John', 'days_off': 4, 'days_for_scrum_commitment': 3, 'min_hours_per_day': 5, 'max_hours_per_day': 8}
            ]

    def test_calculate_available_hours(self):
        instance = FeatureB()
        team_members_details = [
            {'name': 'Alice', 'days_off': 2, 'days_for_scrum_commitment': 2, 'min_hours_per_day': 8, 'max_hours_per_day': 10},
            {'name': 'Bob', 'days_off': 1, 'days_for_scrum_commitment': 2, 'min_hours_per_day': 4, 'max_hours_per_day': 7},
            {'name': 'John', 'days_off': 4, 'days_for_scrum_commitment': 3, 'min_hours_per_day': 5, 'max_hours_per_day': 8}
        ]
        expected_result = [
            {'name': 'Alice', 'days_off': 2, 'days_for_scrum_commitment': 2, 'min_hours_per_day': 8, 'max_hours_per_day': 10, 'available_hours': '48-60'},
            {'name': 'Bob', 'days_off': 1, 'days_for_scrum_commitment': 2, 'min_hours_per_day': 4, 'max_hours_per_day': 7, 'available_hours': '28-49'},
            {'name': 'John', 'days_off': 4, 'days_for_scrum_commitment': 3, 'min_hours_per_day': 5, 'max_hours_per_day': 8, 'available_hours': '15-24'}
        ]
        assert instance.calculate_available_hours(sprint_days=10, team_members_details=team_members_details) == (expected_result, 91, 133)
        
    