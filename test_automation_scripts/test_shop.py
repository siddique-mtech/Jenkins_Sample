import pytest
import logging

@pytest.mark.fruits
def test_apple():
   logging.info("This is Apple function")

@pytest.mark.fruits
def test_banana():
   logging.info("This is Banana function")

@pytest.mark.veg
def test_carrot():
    logging.info("This is ADD function")
  
@pytest.mark.veg
def test_beetroote():
    logging.info("This is DIVIDE function")
