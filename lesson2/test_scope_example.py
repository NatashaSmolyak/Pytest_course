import pytest

@pytest.fixture(scope='class')
def class_fixture():
    print("\n ----Setting up the class fixture---")
    yield
    print("\n ----Tearing down the class fixture---")

@pytest.mark.usefixtures("class_fixture")
class TestClass:

    def test_one(self):
        print('\n Executing test_one')
        assert True

    def test_two(self):
        print('\n Executing test_two')
        assert 1 == 1

def test_outside_class():
    print('\n Executing test outside of the class')
    assert 'a' == 'a'

# для запуска необходимо использовать
# pytest -s -v --setup-show test_scope_example.py
