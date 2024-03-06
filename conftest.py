import pytest
import helpers


@pytest.fixture
def user():
    user = helpers.create_test_user()
    yield user
    helpers.del_user(user["json"]["accessToken"])