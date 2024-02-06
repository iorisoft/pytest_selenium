import math

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("num1, num2, expected_total",
                         [
                             ("10", "10", "20"),
                             ("25", "25", "50"),
                             ("40", "30", "70"),
                             ("122.4", "38.6", "161"),
                             ("7", "43", "50"),
                             ("15", "15", "30")
                         ])
def test_lambdatest_two_input_fields(num1, num2, expected_total):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    driver.find_element(By.ID, ("sum1")).send_keys(num1)
    driver.find_element(By.ID, ("sum2")).send_keys(num2)
    driver.find_element(By.XPATH, ("//button[contains(text(), 'Get Sum')]")).click()
    actual_result = driver.find_element(By.ID, "addmessage").text
    assert expected_total == actual_result, "Actual & Expected Total Do Not Match"



@pytest.mark.parametrize("base", [1,2,3])
@pytest.mark.parametrize("exponent", [4,5,6])
def test_raising_base_to_power(base, exponent):
    resutl = base ** exponent
    assert resutl == math.pow(base,exponent)