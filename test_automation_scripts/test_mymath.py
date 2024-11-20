import pytest

@pytest.mark.logical
def test_and():
   print ("This is AND function")

@pytest.mark.logical
def test_or():
   print ("This is OR function")

@pytest.mark.arithemetic
def test_add():
    print ("This is ADD function")
  
@pytest.mark.arithemetic
def test_divide():
    print ("This is DIVIDE function")
