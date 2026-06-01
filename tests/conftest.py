import copy
import pytest
from src.app import activities


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities to initial state before and after each test"""
    initial_activities = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(copy.deepcopy(initial_activities))
