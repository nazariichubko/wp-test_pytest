import pytest
from src.generators.player import Player

@pytest.fixture()
def get_user_data_generated():
    return Player()