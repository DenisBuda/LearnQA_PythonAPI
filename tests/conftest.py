import pytest

@pytest.fixture(autouse=True)
def say_something():
    # something_text = "Helli"
    # return something_text
    print("Hello")
    return 1