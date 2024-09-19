import pytest


@pytest.mark.parametrize("name", ["John", "Doe"])
def test_validation(name):
    assert name != None


@pytest.mark.parametrize("name, password", [("John", "john@123")])
def test_loginData(name, password):
    assert ["John", "john@123"] == [name, password]

# using params with fixture
@pytest.fixture(scope="module", params=["www.google.com", "www.amazon.in"])
def val(request):
    return request.param

def test_val(val):
    assert val != None
