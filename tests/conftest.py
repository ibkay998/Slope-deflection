import pytest

@pytest.fixture 
def client():
    def _client(name):
        return NewApp(name)
    return _client

@pytest.fixture
def custom_mocker(mocker):
    mock_instance = mocker.patch('test_app.custom_result')
    mock_instance.return_value = 2
    return mock_instance