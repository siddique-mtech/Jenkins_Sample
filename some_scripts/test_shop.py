import pytest

print ("This is Jenkins traning, I am from test_shop")

@pytest.mark.fruits
def test_apple():
   print ("This is Apple function")

@pytest.mark.fruits
def test_banana():
   print ("This is Banana function")

@pytest.mark.veg
def test_carrot():
    print ("This is ADD function")
  
@pytest.mark.veg
def test_beetroote():
    print ("This is DIVIDE function")
