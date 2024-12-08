import pytest

@pytest.mark.profile
def test_methodA():
    print("This is method A")


@pytest.mark.profile
def test_methodB():
    print("This is method B")


def test_Example1():
    print("This is Example1 method")


def test_Example2():
    print("This is Example2 method")