import pytest
import mock
from feature_a import feature_a

class TestFeatureA:
    
    
    def test_input_sprint_points(self):
        instance = feature_a()
        mock_input = mock.Mock()
        mock_input.side_effect = [9,100,110,80,120,95,105,90,110,90]
        sprint_points = [100,110,80,120,95,105,90,110,90]
        with mock.patch('builtins.input', mock_input):
            assert instance.input() == sprint_points
        
    @pytest.mark.parametrize("sprint_points, expected_average", [
        ([100,110,80,120,95,105,90,110,90],100),
        ([150,200,125,175],162.5),
        ([-250,250,200,240,200],128),
        ([-80,-70,-50,-90,-110],-80),
        ([],0)
    ])
    def test_avg_calculation(self,sprint_points,expected_average):
        instance = feature_a()
        assert instance.calculate_velocity(sprint_points=sprint_points) == expected_average
