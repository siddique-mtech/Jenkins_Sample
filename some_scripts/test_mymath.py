import pytest

print ("This is Jenkins traning, I am from test_school.py")

@pytest.mark.logical
def test_and():
   print ("This is and function")

@pytest.mark.logical
def test_or():
   print ("This is and function")

@pytest.mark.arithemetic
def test_add():
    print ("This is ADD function")
  
@pytest.mark.arithemetic
def test_divide():
    print ("This is DIVIDE function")
