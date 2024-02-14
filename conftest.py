import pytest
from selenium import webdriver

from utilities.test_data import TestData


@pytest.fixture(params=["chrome", "firefox", "edge"])
def initialize_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()
    elif request.param == "edge":
        driver = webdriver.Edge()
    request.cls.driver = driver
    print("Browser: ", request.param)
    #Agrego datos para ejercicio de Page Object Model
    driver.get(TestData.url)
    driver.maximize_window()
    #fin de Agregar datos para ejercicio de Page Object Model

    yield
    print("Close Driver")
    driver.close()