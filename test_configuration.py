import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class')
def test_driver_setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()
