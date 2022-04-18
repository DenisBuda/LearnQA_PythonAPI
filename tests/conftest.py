import pytest

def _say_something(something_text:str):
    print(f"Private say {something_text}")


@pytest.fixture()
def say_something():
    yield _say_something


@pytest.fixture()
def write_some_text_to_file():
    with  open("Output2.txt", "a") as file:
        content = "Hello, Welcome to Python Tutorial !! \n"
        file.write(content)
        yield
        fileVariable = open('Output2.txt', 'r+')
        fileVariable.truncate(0)
        fileVariable.close()












