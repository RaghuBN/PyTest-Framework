import pytest

@pytest.mark.profile
def test_methodC():
    print("This is method C")


@pytest.mark.profile
def test_methodD():
    print("This is method D")


@pytest.mark.feeds
def test_Example3():
    print("This is Example3 method")


@pytest.mark.feeds
def test_Example4():
    print("This is Example4 method")

