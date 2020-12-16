import pytest
from fixture.application_group import Application_group

@pytest.fixture
def app(request):
    fixture = Application_group()
    request.addfinalizer(fixture.destroy)
    return fixture