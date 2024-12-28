import pytest
from ..src.dummy import Dummy

def test_greet():
    dummy = Dummy("World")
    assert dummy.greet() == "Hello, World!"

def test_greet_with_another_name():
    dummy = Dummy("Alice")
    assert dummy.greet() == "Hello, Alice!"