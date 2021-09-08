from pytest import fixture
from selenium import webdriver


@fixture(scope = "function")
def chrome_browser():
  chrome_browser = webdriver.Chrome() 
  yield chrome_browser
  
  #* Teardown code
  print("\nI am tearing down...")
