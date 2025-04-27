import pytest
from selenium import webdriver

# Setup fixture with scope mentioned given as Class, hence it will only run once for each Class
@pytest.fixture(scope='class')
def SetUp(request):
    driver = webdriver.Chrome()
    driver.get('https://xaltsocnportal.web.app/signin')
    driver.maximize_window()
    request.cls.driver = driver
    yield 
    driver.quit()

# Setup fixture for Sign in and Sign out tests, they are having the scope as function
@pytest.fixture(scope='function')
def SignInTests(request):
    driver = webdriver.Chrome()
    driver.get('https://xaltsocnportal.web.app/signin')
    driver.maximize_window()
    request.cls.driver = driver
    yield 
    driver.quit()