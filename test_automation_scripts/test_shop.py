import pytest

@pytest.mark.fruits
def test_apple():
   print("This is Apple function")

@pytest.mark.fruits
def test_banana():
   print("This is Banana function")

@pytest.mark.veg
def test_carrot():
   print("This is Carrot function")
  
@pytest.mark.veg
def test_beetroote():
    print("This is Beetroote function")
